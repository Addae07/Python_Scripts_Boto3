import json

# A defined list of languages supported by Amazon Translate
languages = ["af","sq","am","ar","az","bn","bs","bg","zh","zh-TW","hr","cs","da","fa-AF","nl","en","et","fi","fr","fr-CA","ka","de","el","ha","he","hi","hu","id","it","ja","ko","lv","ms","no","fa","ps","pl","pt","ro","ru","sr","sk","sl","so","es","sw","sv","tl","ta","th","tr","uk","ur","vi"]

# This uses a json string as an input
json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr"
        }
    ]
}
"""

json_input = json.loads(json_string)

SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

# Uses an if-elif-else statements to check that the SourceLanguageCode is in the languages list.
if SourceLanguageCode == TargetLanguageCode:
    print("The SourceLanguageCode is the same as the TargetLanguageCode - nothing to do")
elif SourceLanguageCode not in languages and TargetLanguageCode not in languages:
    print("Neither the SourceLanguageCode and TargetLanguageCode are valid - stopping")
elif SourceLanguageCode not in languages:
    print("The SourceLanguageCode is not valid - stopping")
elif TargetLanguageCode not in languages:
    print("The TargetLanguageCode is not valid - stopping")
elif SourceLanguageCode in languages and TargetLanguageCode in languages:
    print("The SourceLanaguageCode and TargetLanguageCode are valid - proceeding")
else:
    print("There is an issue")


#Test
#Test the code by changing the values of the SourceLanguageCode and the TargetLanguageCode.

#Make the SourceLanguageCode and TargetLanguageCode identical values.
#Change the SourceLanguageCode and TargetLanguageCode to different but not valid values.
#Change the SourceLanguageCode to a value not supported and TargetLanguageCode to a supported value.
#Change the SourceLanguageCode to a supported value and the TargetLanguageCode to a not supported value.
#Change both the SourceLanguageCode and TargetLanguageCode to supported but different values.
#What did we do?
#We use our original if statement to check if the source and target languages are equivalent
#We used an and logical operator to check both the SourceLanguageCode and TargetLanguageCode are valid.
#We then used elif a not in combined with the and logical operators to check if neither of the SourceLanguageCode or TargetLanguageCode are valid.
#We then used two elif statements to determine if either the SourceLanguageCode or TargetLanguageCode are valid.

#Finally we used an else statement to catch any other condition.
#What did python do?
#Python checked each of the statements, to see if they returned a True or False. If it returned False, it continues to the next statements in turn to check if they are True or False until it reaches a True statement or else. If it finds a matching statement, it runs the code corresponding to the elif and then skips the rest.
