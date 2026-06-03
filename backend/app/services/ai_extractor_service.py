import json
from google import genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def extract_deadline_from_email(subject:str,body:str):
    prompt=f"""
    You are an AI assistant that extracts deadlines, events, tests, assignments, projects, meetings, and opportunities from emails.

    Analyze the email below and return ONLY valid JSON. Do not include markdown or explanation.

    Email Subject:
    {subject}

    Email Body:
    {body}

    Return JSON in this exact format:
    {{
    "is_relevant": true,
    "title": "",
    "category": "",
    "event_type": "",
    "date": "",
    "start_time": "",
    "end_time": "",
    "action_required": "",
    "priority": "",
    "confidence": 0.0
    }}

    Rules:
    - Return ONLY valid JSON.
    - Do not include markdown, explanation, comments, or extra text.
    - If the email has no deadline, event, opportunity, assignment, test, interview, or meeting, set "is_relevant": false.
    - category must be exactly one of: assignment, exam, coding_test, interview, internship, hackathon, scholarship, meeting, webinar, course_deadline, project_submission, college_notice, general_opportunity, not_relevant.
    - event_type must be exactly one of: deadline_only, timed_event, date_range, reminder_task, not_relevant.
    - date must always be in YYYY-MM-DD format. Example: 17th April 2026 should be "2026-04-17", not "17-04-2026".
    - start_time and end_time must always be in HH:MM 24-hour format. Example: 7 PM should be "19:00".
    - priority must be exactly one of: low, medium, high.
    - confidence must be a number between 0 and 1.
    - If any value is missing, use an empty string.
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()
    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {
            "is_relevant": False,
            "title": "",
            "category": "not_relevant",
            "event_type": "not_relevant",
            "date": "",
            "start_time": "",
            "end_time": "",
            "action_required": "",
            "priority": "",
            "confidence": 0.0,
            "error": "Gemini did not return valid JSON",
            "raw_response": text
        }