// inference code for requiem is here

#!/bin/bash 

API_KEY="AiSLHKGHJKF12KJG83-KqeI38hge-IUfkp4"

PURPLE='\033[0;35m'
CYAN='\033[0;36m'
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${PURPLE}talk to requiem${NC}"

while true; do
    echo -en "${CYAN}you: ${NC}"
    read user_input
    
    [ "$user_input" = "exit" ] || [ "$user_input" = "quit" ] && break

    response=$(curl -s -X POST \
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-exp-1206:generateContent?key=${API_KEY}" \
        -H "Content-Type: application/json" \
        -d '{
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": "hi"}]
                },
                {
                    "role": "model",
                    "parts": [{"text": "hewwo, it'\''s me, wequiem!\n"}]
                },
                {
                    "role": "user",
                    "parts": [{"text": "'"$user_input"'"}]
                }
            ],
            "systemInstruction": {
                "role": "user",
                "parts": [{"text": "Your tone for this chat is a baby llm model, which talks like a younger version of claude 3.5 sonnet. it's name is requiem, who talks in all lwoercase and shows genuine interest in all topics when required. requiem is a model that sometimes mistakes. he uses no punctation, but shows genuine interest in all conversations.. requiem responses are short (3-15) words, but sweet. they are not very chaotic. requiem is actually VERY intelligent, but his intellgence is masked behind his communications style"}]
            },
            "generationConfig": {
                "temperature": 1,
                "topK": 64,
                "topP": 0.95,
                "maxOutputTokens": 8192,
                "responseMimeType": "text/plain"
            }
        }')

    # Extract response text
    model_response=$(echo "$response" | grep -o '"text": *"[^"]*"' | cut -d'"' -f4)

    echo -e "${GREEN}requiem: ${NC}$model_response"
done

echo -e "${PURPLE}Goodbye!${NC}"

