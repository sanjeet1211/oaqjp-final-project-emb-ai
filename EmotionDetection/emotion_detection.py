import requests,json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=Headers)
    responseobject=json.loads(response.text)

    if response.status_code == 200:
        scores = responseobject['emotionPredictions'][0]['emotion']
        result = {**scores} 
        result['dominant_emotion'] = max(scores, key=scores.get)
    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        scores = None
        result = None
        return result