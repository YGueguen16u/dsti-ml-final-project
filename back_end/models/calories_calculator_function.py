import re

def parse_user_input(text):
    """
    Extract structured info from keyword-style input like:
    "I am a 29-year-old woman, 56 kg., 163 cm., moderately active. I want to lose 2 kg in 2 months."
    """
    text = text.lower()

    # Age
    age_match = re.search(r'(?:i am|i\'m)?\s*(\d+)\s*(?:year[-\s]?old|years?\s?old)', text)

    age = int(age_match.group(1)) if age_match else 30

    # Weight
    weight_match = re.search(r'(\d+\.?\d*)\s*kg', text)
    weight = float(weight_match.group(1)) if weight_match else 60.0

    # Height
    height_match = re.search(r'(\d+\.?\d*)\s*cm', text)
    height = float(height_match.group(1)) if height_match else 160.0

    # Sex
    sex = 'female' if 'woman' in text or 'female' in text else 'male'

    # Activity level
    activity_levels = ['sedentary', 'light', 'moderate', 'active', 'very active']
    activity_level = next((level for level in activity_levels if level in text), 'moderate')

    # Goal
    if 'lose' in text:
        goal = 'lose'
    elif 'gain' in text or 'bulk' in text:
        goal = 'gain'
    else:
        goal = 'maintain'

    # Weight change
    match_weight_change = re.search(r'(lose|gain)\s*(\d+\.?\d*)\s*kg', text)
    target_weight_change_kg = float(match_weight_change.group(2)) if match_weight_change else 0

    # Duration
    match_duration = re.search(r'in\s*(\d+)\s*(week|month|day)', text)
    if match_duration:
        value, unit = int(match_duration.group(1)), match_duration.group(2)
        if 'day' in unit:
            duration_weeks = value / 7
        elif 'month' in unit:
            duration_weeks = value * 4
        else:
            duration_weeks = value
    else:
        duration_weeks = 0

    return {
        "weight_kg": weight,
        "height_cm": height,
        "age": age,
        "sex": sex,
        "activity_level": activity_level,
        "goal": goal,
        "target_weight_change_kg": target_weight_change_kg,
        "duration_weeks": duration_weeks
    }

def calculate_caloric_needs(weight_kg, height_cm, age, sex, activity_level, goal,
                             target_weight_change_kg=0, duration_weeks=0):
    """
    Calculate daily caloric needs and adjustments based on personal goals and timeframe.
    """
    # Step 1: Calculate BMR
    if sex.lower() == 'male':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    elif sex.lower() == 'female':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    else:
        raise ValueError("Sex must be 'male' or 'female'.")

    # Step 2: Activity multiplier
    activity_multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very active': 1.9
    }

    if activity_level.lower() not in activity_multipliers:
        raise ValueError("Invalid activity level.")

    tdee = bmr * activity_multipliers[activity_level.lower()]

    # Step 3: Determine daily caloric adjustment
    daily_adjustment = 0
    if goal.lower() in ['lose', 'gain']:
        if target_weight_change_kg <= 0 or duration_weeks <= 0:
            raise ValueError("For weight loss/gain, both weight_change and duration_weeks must be > 0")

        calories_per_kg = 7700  # kcal per kg of fat
        total_calorie_change = target_weight_change_kg * calories_per_kg
        duration_days = duration_weeks * 7
        daily_adjustment = total_calorie_change / duration_days

        if goal.lower() == 'lose':
            daily_adjustment = -daily_adjustment  # create a deficit

    # Step 4: Final recommended intake
    daily_calories = tdee + daily_adjustment

    return {
        'BMR': round(bmr, 2),
        'TDEE': round(tdee, 2),
        'Daily Caloric Adjustment': round(daily_adjustment, 2),
        'Recommended Daily Calories': round(daily_calories, 2)
    }

user_text = "I am a 29 years old woman, 56 kg., 163 cm., moderately active. I want to lose 2 kg in 2 months."

parsed = parse_user_input(user_text)
print("Parsed input:", parsed)

result = calculate_caloric_needs(**parsed)
for k, v in result.items():
    print(f"{k}: {v}")