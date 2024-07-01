import requests

def generateTrivia():
    url = "https://opentdb.com/api.php?amount=3&encode=url3986"

    response = requests.get(url)
    data = response.json()
    trivia = ""
    if data["response_code"] == 0:
        results = data["results"]
        for result in results:
            question = requests.utils.unquote(result["question"])
            correct_answer = requests.utils.unquote(result["correct_answer"])
            trivia = trivia + "      Question: " + question + " ... 5 ... 4 ... 3 ... 2 ... 1 ... Correct Answer: " + correct_answer

    return trivia

print (generateTrivia())