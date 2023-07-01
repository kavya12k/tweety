function analyzeText()
{
    const userInput = document.getElementById("userInput").value;
  //Send POST request to the backend API
  fetch('http://127.0.0.1:3000/sentiment_analysis', {
    method: 'POST',
    mode: "cors",
    body: JSON.stringify({ input: userInput }),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .then(responseData =>{
    console.log(responseData);
    console.log("HRUHHH RESPONSE DATA IS ABOVEEE")
    const result = document.getElementById("result");
    if (responseData.result.label == "NEG")
    {
      result.innerHTML = "This text is NEGATIVE :("
    }
    else if (responseData.result.label == "POS")
    {
      result.innerHTML = "This text is POSITIVE :)"
    }
    else
    {
      result.innerHTML = "This text is NEUTRAL :|"
    }
})
.catch (error => {
    console.error ('Error', error);
})
}