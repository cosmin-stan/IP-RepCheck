import urllib.request
import json
import xlwt

# Replace 'YOUR_API_KEY'
api_key = 'KEY'

with open('ip_addresses.txt', 'r') as file:
    target_ips = [line.strip() for line in file]

# Create a new Excel workbook and add a worksheet
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet("IP Addresses")

header = ["IP Address", "Criticality Label", "Risk String", "Number of Rules",
          "Criticality", "Risk Summary", "Risk Score", "AI Insights Text", "Number of References"]
for col, header_text in enumerate(header):
    worksheet.write(0, col, header_text)

row = 1 

for target_ip in target_ips:
    url = f'https://api.recordedfuture.com/v2/ip/{target_ip}?fields=risk,aiInsights&metadata=false&taggedText=false'
    req = urllib.request.Request(url, headers={'X-RFToken': api_key})
    
    try:
        with urllib.request.urlopen(req) as res:
            data = res.read()
            decoded_data = data.decode('utf-8')
            
            # Parse the JSON response
            response_json = json.loads(decoded_data)
            
            # Extract risk information
            risk_data = response_json.get('data', {}).get('risk', {})
            
            # Extract aiInsights information
            ai_insights = response_json.get('data', {}).get('aiInsights', {})
            
            # Write data to Excel
            worksheet.write(row, 0, target_ip)
            
            if risk_data:
                worksheet.write(row, 1, risk_data.get('criticalityLabel', 'N/A'))
                worksheet.write(row, 2, risk_data.get('riskString', 'N/A'))
                worksheet.write(row, 3, risk_data.get('rules', 'N/A'))
                worksheet.write(row, 4, risk_data.get('criticality', 'N/A'))
                worksheet.write(row, 5, risk_data.get('riskSummary', 'N/A'))
                worksheet.write(row, 6, risk_data.get('score', 'N/A'))
            
            if ai_insights:
                worksheet.write(row, 7, ai_insights.get('text', 'N/A'))
                worksheet.write(row, 8, ai_insights.get('numberOfReferences', 'N/A'))
            
            row += 1
        
    except urllib.error.HTTPError as e:
        print(f"Error for IP Address {target_ip}: {e}")

# Save the Excel file
workbook.save("ip_addresses.xls")
