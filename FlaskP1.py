from flask import Flask, render_template, request, redirect, url_for
# Initialize the Flask app
app = Flask(__name__)

diary_entries = []

@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Diary Entries</h1>
    """
    # Check if there are any entries
    if diary_entries:
        for i, entry in enumerate(diary_entries, start=1):
            sentiment = sentiment_checker(entry)
            html += f"""
            <p>Day {i}: {entry} <br>
            \nSentiment: {sentiment}</p>
            <a href="/delete/{i-1}" style="color: red;">Delete</a>
            </p>
            """
    else:
        html += "<p>No entries yet!</p>"

    html += """
        <h2>Add a New Entry</h2>
        <form action="/add" method="post">
            <input type="text" name="entry" placeholder="Write your diary entry" required>
            <button type="submit">Add Entry</button>
        </form>
    </body>
    </html>
    """
    return html

@app.route('/add', methods=['POST'])
def add_entry():
    entry = request.form.get('entry')  # Get user input from the form
    if entry:
        diary_entries.append(entry)  # Add the entry to your list
    return redirect(url_for('index'))  # Redirect to the homepage
@app.route('/delete/<int:entry_id>')
def delete_entry(entry_id):
    if 0 <= entry_id < len(diary_entries):
        diary_entries.pop(entry_id)
    return redirect(url_for('index'))

happy_words = ["happy","awesome","knocked em'out","hell yeah","win"]
sad_words = ["sad","hurt","alone","cried","broken"]
def sentiment_checker(entry):
    happy_count = sum(1 for word in happy_words if word in entry.lower())
    sad_count = sum(1 for word in sad_words if word in entry.lower())
    if happy_count > sad_count:
        return "Happy day, enjoy it baby!"
    else:
        return "Sad day, you'll get em next time champ!"
def highlig
# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
