# Remedy
*The "Remedy.ipynb" file is the notebook used to run the Remedy application in Google Collab while "Fine_tune_Llama_2_in_Google_Colab.ipynb" in the training folder was the notebook used to train the model and was created by [@maximelabonne](https://twitter.com/maximelabonne)  
## Inspiration
With the rise of general use large language models like Chatgpt and Gemini, we became inspired to create something more niche that would help benefit the healthcare industry.
## What it does
Remedy is a personalized health companion for comprehensive well-being. It is an advanced Language Model designed specifically for healthcare, empowering users to access information and advice from the comfort of their homes. With Remedy, you can inquire about general health concerns, receive insights on wellness practices, and gain valuable recommendations tailored to your unique needs.
## How we built it
The training process consisted of finetuning a base model using a method known as LoRa or Low-Rank Adaptation. This works by Reducing the number of trainable parameters by examining the model parameters as a matrix and Fine-tuning two smaller matrices that approximate a larger matrix,
Updating only a small part of the model's weights, specifically targeting those with the most significant impact on the task. After this, we insert a smaller number of new weights into the model which we then train on. We trained our model using this colab [notebook](https://colab.research.google.com/drive/1PEQyJO1-f6j0S_XJ8DV50NkpzasXkrzd?usp=sharing) and used Meta's llama 2 opensource llm as the base model. More specifically we used the  Llama-2-7B-bf16-sharded model found [here](https://huggingface.co/TinyPixel/Llama-2-7B-bf16-sharded)  
  
We used [this](https://huggingface.co/datasets/keivalya/MedQuad-MedicalQnADataset) dataset of medical questions and answers which consisted of 16.4k examples. We trained the model on 9.8k of these examples and planned on using the rest for testing, however, we did not have enough time to properly test all of the testing sets.  
  
We then built a simple chat application using Flask and used the Hugging face transformer library to run our model and interact with it. We then deployed this application on google colab to use cloud resources since none of our computers were powerful enough to run the model.  

The final model and all its files can be found [here](https://drive.google.com/drive/folders/1LdoQnVC8ag_XkaVxUOb1HY6yqhW9eg1e?usp=drive_link)

## Challenges we ran into
One major challenge we ran into was hardware as we quickly found out that training and using a LLM is a very resource-heavy process that none of our machines could handle. We found a workaround to this issue through the use of cloud computing and google colab, which gave us access to resources that made this project possible in the first place.  
 
## Accomplishments that we're proud of
Something we were proud of was the front end as this was 2 of our member's first time coding.  So going through the process and creating a whole application was very difficult for them but they still managed to pull through.  
  
Another accomplishment was managing to find workarounds in deploying a Flask application on a cloud-based system as its normally very uncommon to host web applications on a notebook such as google colab. Managing to get everything working with the hugging face libraries was a big achievement.

## What we learned
Building Remedy has been a comprehensive journey, encompassing various technologies and methodologies. Leveraging Google Colab, we honed our collaborative coding skills, fostering an efficient development environment. Python Flask web development facilitated the creation of a user-friendly interface, ensuring seamless interaction. The integration of the Hugging Face Transformer library allowed us to harness the power of state-of-the-art language models, enabling Remedy to comprehend and respond to user queries with precision. Throughout the process, we gained valuable insights into the intricate workings of Large Language Models (LLMs), understanding their capabilities and fine-tuning parameters for optimal performance. This multifaceted experience has not only deepened our technical proficiency but also underscored the potential of these technologies to revolutionize personalized healthcare solutions.

## What's next for Remedy
In shaping the future of healthcare assistance, Remedy is committed to refining its generation parameters for increased accuracy and enforcing a proper token cutoff. Ongoing fine-tuning ensures a more precise and relevant output, minimizing repetition and eliminating unnecessary information. Our dedication to continuous improvement positions Remedy as a dynamic virtual health companion, evolving alongside the latest advancements in natural language processing. The future of Remedy promises an even more sophisticated and tailored experience, empowering users with unparalleled insights for optimal health and wellness decision-making.
