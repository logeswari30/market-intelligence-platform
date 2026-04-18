import google.generativeai as genai

# ⚠️ Your API Key (temporary use only)
genai.configure(api_key="api key")

def analyze_data(data):
    try:
        model = genai.GenerativeModel("gemini-pro")

        prompt = f"""
        You are a financial analyst.

        Analyze the following market data and provide:
        1. Overview
        2. Opportunities
        3. Risks
        4. Conclusion

        Data:
        {data}
        """

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"AI Error: {str(e)}"
