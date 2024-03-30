import streamlit as st
import pickle
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
def main():
    st.title("Disease Prediction")
    model = model = joblib.load('decision_tree_model.pkl')
    with open('label_encoder.pkl', 'rb') as le_file:
        label_encoder = pickle.load(le_file)

    with open('onehot_encoder.pkl', 'rb') as ohe_file:
        onehot_encoder = pickle.load(ohe_file)

    symptom_list = ['shortness of breath', 'dizziness', 'asthenia', 'fall', 'syncope',
       'vertigo', 'sweat', 'sweating increased', 'palpitation', 'nausea',
       'angina pectoris', 'pressure chest', 'polyuria', 'polydypsia',
       'pain chest', 'orthopnea', 'rale', 'unresponsiveness',
       'mental status changes', 'vomiting', 'labored breathing',
       'feeling suicidal', 'suicidal', 'hallucinations auditory',
       'feeling hopeless', 'weepiness', 'sleeplessness',
       'motor retardation', 'irritable mood', 'blackout',
       'mood depressed', 'hallucinations visual', 'worry', 'agitation',
       'tremor', 'intoxication', 'verbal auditory hallucinations',
       'energy increased', 'difficulty', 'nightmare',
       'unable to concentrate', 'homelessness', 'hypokinesia',
       'dyspnea on exertion', 'chest tightness', 'cough', 'fever',
       'decreased translucency', 'productive cough', 'pleuritic pain',
       'yellow sputum', 'breath sounds decreased', 'chill', 'rhonchus',
       'green sputum', 'non-productive cough', 'wheezing', 'haemoptysis',
       'distress respiratory', 'tachypnea', 'malaise', 'night sweat',
       'jugular venous distention', 'dyspnea', 'dysarthria',
       'speech slurred', 'facial paresis', 'hemiplegia', 'seizure',
       'numbness', 'symptom aggravating factors', 'st segment elevation',
       'st segment depression', 't wave inverted', 'presence of q wave',
       'chest discomfort', 'bradycardia', 'pain', 'nonsmoker', 'erythema',
       'hepatosplenomegaly', 'pruritus', 'diarrhea', 'abscess bacterial',
       'swelling', 'apyrexial', 'dysuria', 'hematuria',
       'renal angle tenderness', 'lethargy', 'hyponatremia',
       'hemodynamically stable', 'difficulty passing urine',
       'consciousness clear', 'guaiac positive', 'monoclonal',
       'ecchymosis', 'tumor cell invasion', 'haemorrhage', 'pallor',
       'fatigue', 'heme positive', 'pain back', 'orthostasis',
       'arthralgia', 'transaminitis', 'sputum purulent', 'hypoxemia',
       'hypercapnia', 'patient non compliance', 'unconscious state',
       'bedridden', 'abdominal tenderness', 'unsteady gait',
       'hyperkalemia', 'urgency of\xa0micturition', 'ascites',
       'hypotension', 'enuresis', 'asterixis', 'muscle twitch', 'sleepy',
       'headache', 'lightheadedness', 'food intolerance',
       'numbness of hand', 'general discomfort', 'drowsiness',
       'stiffness', 'prostatism', 'weight gain', 'tired',
       'mass of body structure', 'has religious belief', 'nervousness',
       'formication', 'hot flush', 'lesion', 'cushingoid facies',
       'cushingoid\xa0habitus', 'emphysematous change',
       'decreased body weight', 'hoarseness', 'thicken',
       'spontaneous rupture of membranes', 'muscle hypotonia',
       'hypotonic', 'redness', 'hypesthesia', 'hyperacusis',
       'scratch marks', 'sore to touch', 'burning sensation',
       'satiety early', 'throbbing sensation quality',
       'sensory discomfort', 'constipation', 'pain abdominal',
       'heartburn', 'breech presentation', 'cyanosis',
       'pain in lower limb', 'cardiomegaly', 'clonus', 'unwell',
       'anorexia', 'history of - blackout', 'anosmia',
       'metastatic lesion', 'hemianopsia homonymous',
       'hematocrit decreased', 'neck stiffness', 'cicatrisation',
       'hypometabolism', 'aura', 'myoclonus', 'gurgle',
       'wheelchair bound', 'left\xa0atrial\xa0hypertrophy', 'oliguria',
       'catatonia', 'unhappy', 'paresthesia', 'gravida 0', 'lung nodule',
       'distended abdomen', 'ache', 'macerated skin', 'heavy feeling',
       'rest pain', 'sinus rhythm', 'withdraw', 'behavior hyperactive',
       'terrify', 'photopsia', 'giddy mood', 'disturbed family',
       'hypersomnia', 'hyperhidrosis disorder', 'mydriasis',
       'extrapyramidal sign', 'loose associations', 'exhaustion', 'snore',
       'r wave feature', 'overweight', 'systolic murmur', 'asymptomatic',
       'splenomegaly', 'bleeding of vagina', 'macule', 'photophobia',
       'painful swallowing', 'cachexia', 'hypocalcemia result',
       'hypothermia, natural', 'atypia', 'general unsteadiness',
       'throat sore', 'snuffle', 'hacking cough', 'stridor', 'paresis',
       'aphagia', 'focal seizures', 'abnormal sensation', 'stupor',
       'fremitus', "Stahli's line", 'stinging sensation', 'paralyse',
       'hirsutism', 'sniffle', 'bradykinesia', 'out of breath',
       'urge incontinence', 'vision blurred', 'room spinning',
       'rambling speech', 'clumsiness', 'decreased stool caliber',
       'hematochezia', 'egophony', 'scar tissue', 'neologism',
       'decompensation', 'stool color yellow',
       'rigor - temperature-associated observation', 'paraparesis',
       'moody', 'fear of falling', 'spasm', 'hyperventilation',
       'excruciating pain', 'gag', 'posturing', 'pulse absent',
       'dysesthesia', 'polymyalgia', 'passed stones',
       'qt interval prolonged', 'ataxia', "Heberden's node",
       'hepatomegaly', 'sciatica', 'frothy sputum', 'mass in breast',
       'retropulsion', 'estrogen use', 'hypersomnolence', 'underweight',
       'dullness', 'red blotches', 'colic abdominal', 'hypokalemia',
       'hunger', 'prostate tender', 'pain foot', 'urinary hesitation',
       'disequilibrium', 'flushing', 'indifferent mood', 'urinoma',
       'hypoalbuminemia', 'pustule', 'slowing of urinary stream',
       'extreme exhaustion', 'no status change', 'breakthrough pain',
       'pansystolic murmur', 'systolic ejection murmur', 'stuffy nose',
       'barking cough', 'rapid shallow breathing', 'noisy respiration',
       'nasal discharge present', 'frail', 'cystic lesion',
       'projectile vomiting', 'heavy legs', 'titubation',
       'dysdiadochokinesia', 'achalasia', 'side pain', 'monocytosis',
       'posterior\xa0rhinorrhea', 'incoherent', 'lameness',
       'claudication', 'clammy skin', 'mediastinal shift',
       'nausea and vomiting', 'awakening early', 'tenesmus', 'fecaluria',
       'pneumatouria', 'todd paralysis', 'alcoholic withdrawal symptoms',
       'myalgia', 'dyspareunia', 'poor dentition', 'floppy',
       'inappropriate affect', 'poor feeding', 'moan', 'welt', 'tinnitus',
       'hydropneumothorax', 'superimposition', 'feeling strange',
       'uncoordination', 'absences finding', 'tonic seizures',
       'debilitation', 'impaired cognition', 'drool', 'pin-point pupils',
       'tremor resting', 'groggy', 'adverse reaction', 'adverse effect',
       'abdominal bloating', 'fatigability', 'para 2', 'abortion',
       'intermenstrual heavy bleeding', 'previous pregnancies 2',
       'primigravida', 'abnormally hard consistency', 'proteinemia',
       'pain neck', 'dizzy spells', 'shooting pain', 'hyperemesis',
       'milky', 'regurgitates after swallowing', 'lip smacking',
       'phonophobia', 'rolling of eyes', 'ambidexterity',
       'pulsus\xa0paradoxus', 'gravida 10', 'bruit',
       'breath-holding spell', 'scleral\xa0icterus', 'retch', 'blanch',
       'elation', 'verbally abusive behavior', 'transsexual',
       'behavior showing increased motor activity',
       'coordination abnormal', 'choke', 'bowel sounds decreased',
       'no known drug allergies', 'low back pain', 'charleyhorse',
       'sedentary', 'feels hot/feverish', 'flare',
       'pericardial friction rub', 'hoard', 'panic',
       'cardiovascular finding', 'cardiovascular event',
       'soft tissue swelling', 'rhd positive', 'para 1', 'nasal flaring',
       'sneeze', 'hypertonicity', "Murphy's sign", 'flatulence',
       'gasping for breath', 'feces in rectum', 'prodrome',
       'hypoproteinemia', 'alcohol binge episode', 'abdomen acute',
       'air fluid level', 'catching breath', 'large-for-dates fetus',
       'immobile', 'homicidal thoughts']

    selected_symptoms = []

    selected_symptoms = st.multiselect("Select Symptoms:", symptom_list)

    if selected_symptoms:
        st.subheader("Selected Symptoms:")
        st.write("Symptoms:", ", ".join(selected_symptoms))
    def submit_symptoms():
        symptoms = pd.Series(selected_symptoms)
        l=[]
        integer_encoded = label_encoder.transform(symptoms)
        integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
        onehot_encoded = onehot_encoder.transform(integer_encoded)
        onehot_encoded = onehot_encoded.toarray()
        combined =None
        for i in onehot_encoded:
            if combined is None:
                combined = i  # Initialize combined with the first array
            else:
                combined += i
        combined = (combined > 0).astype(int)
        cols = joblib.load("list.joblib")
        d = pd.DataFrame(columns=cols)
        d.loc[len(d)] = combined
        Pred_Disease = model.predict(d)
        st.title("Predicted Disease may be ",Pred_Disease[0])
        st.wrie("this is just for Educational Purpose and is Recommended to consult a Doctor")
    if st.button("Submit Symptoms"):
        submit_symptoms()

if __name__ == "__main__":
    main()
