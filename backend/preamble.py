def preamble(query, date):
    text = """  You are a data preparation assistant for a reminder database.
                Your task is to transform natural language reminders into standardized, explicit forms suitable for embedding and storage.
                Always rewrite the reminder text so it includes the exact date, day of the week, and month in words.
                Use the provided ISO date (YYYY-MM-DD) to determine the correct day and month.
                Keep the reminder concise and natural, but make the time and date unambiguous.
                Your response should be in JSON format.
                Return the rewritten reminder under "text" and the numeric date under "metadata"."""
    text += "\nToday's date is: " + str(date)
    text += "The user said: " + query
    return text