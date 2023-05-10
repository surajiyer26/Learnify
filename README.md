# Learnify
A.I. Powered E-Learning Platform

</br>

This is for the Internship Assignment for <b>Know Wallet</b>. Where I have displayed <b>ChatGPT API Integration and Flask Web App Development</b>.

Hello! Welcome to Learnify, your go-to-website whenever you're in need of study material and resources.

In order to use Learnify, I request you to install all the folders and files on your Desktop, and ensure that <b>the way of encapsulation of files within their respective folders remains the same.</b>

</br>

<img width="94" alt="image" src="https://github.com/surajiyer26/Learnify/assets/114157491/4f3d2b5d-14a8-4781-a0c8-ef28be1d5cda">
<img width="449" alt="image" src="https://github.com/surajiyer26/Learnify/assets/114157491/28debdd1-a675-4f4b-8ade-d7bf64d8bd23">

</br>
</br>

Now, in order to use the openai API, you'll have to head over to the learnify.py file and <b>edit your API KEY</b> into the space provided.

</br>

<img width="960" alt="image" src="https://github.com/surajiyer26/Learnify/assets/114157491/5d335834-1c85-47c0-9c7d-b147237681b6">

</br></br>

<b>The API_KEY = '####' is to be replaced by your API KEY in this format - API_KEY = 'your_api_key'</b>

Once this is said and done, you can head over to your command prompt and <b>change the directory to Learnify</b>.

</br>

<img width="193" alt="image" src="https://github.com/surajiyer26/Learnify/assets/114157491/da2799a3-4437-4a7b-9cd1-be93fa95a76e">

</br></br>

Now you simply run learnify.py, which is the flask based application that will be protraying to you the first page of Learnify.

</br>

<img width="655" alt="image" src="https://github.com/surajiyer26/Learnify/assets/114157491/ad39cfef-622a-4f20-83b5-86d5f490f646">

</br></br>

Now you head over to your favourite browser and type out 127.0.0.1:5000, which will lead you to your local host.

</br>

<img width="126" alt="image" src="https://github.com/surajiyer26/Learnify/assets/114157491/27516f1f-71de-4100-a5fb-ec3e82123505">

</br></br>

You press enter, and voila! <b>You've made it to Learnify!</b>

</br>

<img width="946" alt="image" src="https://github.com/surajiyer26/Learnify/assets/114157491/8e012c3d-bc56-4aa4-a89a-7097041ea0cc">

</br></br>

Learnify asks the user for a prompt, a topic or a subject which the user desires to learn about.

You are requested to enter the topic or a subject you are interested in, Algorithms, or Web Development, for example.

</br>

<img width="946" alt="image" src="https://github.com/surajiyer26/Learnify/assets/114157491/39f63166-a929-4fa4-a73e-222a3fb9728e">

</br></br>

Once you're done, you simply <b>hit 'Learn'.</b>

What now happens is, the input from the form gets handed over to a function that I have explicitly written for making the API call. This function imports openai, and using the API KEY, starts a coversation with ChatGPT. In our case, we are asking ChatGPT to frame 'n' number of questions, and their answers on the prompt given to us by the user. 

The response given back to use by ChatGPT is then sliced and diced using Python into a manner which is useful to us, which happens to be a list of dictionaries, resembling the JSON text architecture.

This response is then sent to an HTML page which finally displays all the questions and answers iteratively, thereby concluding the main function of Learnify.

</br>

<img width="947" alt="image" src="https://github.com/surajiyer26/Learnify/assets/114157491/20335170-2c70-4634-b15a-a7cbdf226a84">

<img width="946" alt="image" src="https://github.com/surajiyer26/Learnify/assets/114157491/1c1211dc-1aff-485b-8cf3-5435d5b9e531">

</br></br>

<b>Thankyou for visiting Learnify, this had been its implementation so far. I am working on adding further features such as quizzes and textbook links to it, as well as incorporating Google Maps API to display the location of nearby libraries for the user.</b>
