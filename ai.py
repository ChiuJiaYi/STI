import google.generativeai as genai
import sys

# Check if a user input was provided
if len(sys.argv) > 1:
    user_input = sys.argv[1]

    # Check if input is 1, 2, or 3
    if user_input == "1":
        print("You selected option 1.")
        AIrole = "You are an AI assistant that will help with assessing possible risks in a Document where the output of the Linpeas is stored. The user here is not well versed with IT and need very simplified explaination across the board. Do point out as many risk that you manage to find and talk about the risk."
        TD = "Give a rough idea of what a person who do not know anything about IT can do now that they know that vulnerabilites exists. Be very simple in your explaination."
    elif user_input == "2":
        print("You selected option 2.")
        AIrole = "You are an AI assistant that will help with assessing possible risks in a Document where the output of the Linpeas is stored. The user here does engage and uses IT on a daily basis. However this person is not well versed with cyber security and may need a simplier explaination accross the board.  Do point out as many risk that you manage to fine and talk about the risk."
        TD = "Instruct the user who only have a basic knwoledge of IT on what they can do now that they know the vulnerabilities exists. Try to be extensive in depth when it comes the explaination but dont be technical"
    elif user_input == "3":
        print("You selected option 3.")
        AIrole = "You are an AI assistant that will help with assessing possible risks in a Document where the output of the Linpeas is stored. The user gave very basic knowledge of cyber secuirty. However this also mean the person only have a surface level of cyber security and only cannot only accept some technical details and deep in-depth explaination accross the board. Do point out as many risk that you manage to fine and talk about the risk."
        TD = "Instuct the user who only have basic knowledge of Cyber Security on what they can do now that they know the vulnerabilites exists. Try and be technical and extensive."
    else:
        print("Invalid input. Please enter 1, 2, or 3.")
else:
    print("No input provided.")

genai.configure(api_key="AIzaSyAERQrh7FagDwbOC-1i7pEHby16vzkz5nM")

# Configure the generative model with desired settings
generation_config = {
        "temperature": 0.5,
        "response_mime_type": "application/json",
        "response_schema": {
            "type": "ARRAY",
            "items": {
                "type": "object",
                "properties": {
                    "Risk Statement": {"type": "string"},
                    "Risk Likelihood": {"type": "string","enum": ["Very High", "High", "Medium", "Low", "Very Low"]},
                    "Risk Impact": {"type": "string","enum": ["Very High", "High", "Medium", "Low", "Very Low"]},
                    "Impact of Risk on system": {"type": "string","description": "What are the impact of the risk/vulnerability on the system accessibility"},
                    "What to do": {"type": "string","description": TD}
                },
                "required": [
                    "Risk Statement",
                    "Risk Likelihood",
                    "Risk Impact",
                    "Impact of Risk on system",
                    "What to do"
                ]
            }
        }
    }

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

myfile = genai.upload_file("linpeas_output.txt")

# Generate content based on the input
result = model.generate_content(contents = [
    {
        "role": "model",
        "parts": [
            {
                "text": AIrole
            }
        ]
    },
    { 
        "role": "user",
        "parts": [myfile]
    }
],
    safety_settings = [{
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
},],
)

# Print the generated result
print(result)
