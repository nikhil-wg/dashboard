from flask import Flask, render_template

app = Flask(__name__)

# Sample data obtained from your Python program (replace this with your actual data retrieval logic)
data = [
    {
        "Name": "durvesh resume",
        "Email": "pedurveshwagh11@gmail.com",
        "LinkedIn ID": "linkedin.com/durvesh-wagh",
        "Phone Number": 7219365109.0,
        "Education": None,
        "Experience": None,
        "Score": 15
    },
    {
        "Name": "1",
        "Email": "Not found",
        "LinkedIn ID": None,
        "Phone Number": None,
        "Education": None,
        "Experience": "5 years of experience",
        "Score": 10
    },
    {
        "Name": "Harcharan  Resume  final year ",
        "Email": "harcharansingh198400@gmail.com",
        "LinkedIn ID": None,
        "Phone Number": 6283343351.0,
        "Education": None,
        "Experience": None,
        "Score": 10
    },
    {
        "Name": "resume dutt",
        "Email": "Not found",
        "LinkedIn ID": None,
        "Phone Number": None,
        "Education": None,
        "Experience": None,
        "Score": 7
    },
    {
        "Name": "Piyush kahale",
        "Email": "pepyush671@gmail.com",
        "LinkedIn ID": None,
        "Phone Number": 9623810879.0,
        "Education": None,
        "Experience": None,
        "Score": 4
    },
    {
        "Name": "5",
        "Email": "Not found",
        "LinkedIn ID": None,
        "Phone Number": None,
        "Education": None,
        "Experience": None,
        "Score": 1
    },
    {
        "Name": "7",
        "Email": "Not found",
        "LinkedIn ID": None,
        "Phone Number": None,
        "Education": None,
        "Experience": None,
        "Score": 0
    }
]

@app.route('/')
def index():
    return render_template('./template/demo.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
