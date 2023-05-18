from django.shortcuts import render
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# Create your views here.
def run_webdriver(request):
    if request.method == 'POST':
        website_url = request.POST.get('website_url', '')
        
        # Set up ChromeDriver with the latest version
        driver = webdriver.Chrome(ChromeDriverManager().install())
        
        try:
            # Navigate to the website URL
            driver.get(website_url)
            
            # Further actions using the web driver
            
            success_message = "Web Driver executed successfully!"
            return render(request, 'webdriver_app/webdriver.html', {'success_message': success_message})
        except Exception as e:
            error_message = f"Error occurred: {str(e)}"
            return render(request, 'webdriver_app/webdriver.html', {'error_message': error_message})
        finally:
            # Quit the driver to release resources
            driver.quit()
    
    return render(request, 'webdriver_app/webdriver.html')
