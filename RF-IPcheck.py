import urllib.request
import json

# 'YOUR_API_KEY'
api_key = 'KEY'

with open('ip_addresses.txt', 'r') as file:
    target_ips = [line.strip() for line in file]

for target_ip in target_ips:
    url = f'https://api.recordedfuture.com/v2/ip/{target_ip}?fields=risk,aiInsights&metadata=false&taggedText=false'
    req = urllib.request.Request(url, headers={'X-RFToken': api_key})
    
    try:
        with urllib.request.urlopen(req) as res:
            data = res.read()
            decoded_data = data.decode('utf-8')
            
            response_json = json.loads(decoded_data)
            
            risk_data = response_json.get('data', {}).get('risk', {})
            
            if risk_data:
                print(f"IP Address: {target_ip}")
                print("Criticality Label:", risk_data.get('criticalityLabel', 'N/A'))
                print("Risk String:", risk_data.get('riskString', 'N/A'))
                print("Number of Rules:", risk_data.get('rules', 'N/A'))
                print("Criticality:", risk_data.get('criticality', 'N/A'))
                print("Risk Summary:", risk_data.get('riskSummary', 'N/A'))
                print("Risk Score:", risk_data.get('score', 'N/A'))
            
            ai_insights = response_json.get('data', {}).get('aiInsights', {})
            
            if ai_insights:
                print("AI Insights:")
                print("Text:", ai_insights.get('text', 'N/A'))
                print("Number of References:", ai_insights.get('numberOfReferences', 'N/A'))
                
            print("------------------------")
        
    except urllib.error.HTTPError as e:
        print(f"Error for IP Address {target_ip}: {e}")
