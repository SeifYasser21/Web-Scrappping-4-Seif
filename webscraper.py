import requests
from bs4 import BeautifulSoup
import csv

# Create a CSV file for the output
csv_file = open('output.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Company Name', 'Company URL', 'Project No.', 'Project Location', 'Project URL'])

# Loop through all pages
total_pages = 351
for page in range(1, total_pages + 1):
    url = f'https://teduh.kpkt.gov.my/developer-swasta?page={page}'
    response = requests.get(url)

    if response.status_code == 200:
        soup1 = BeautifulSoup(response.text, 'html.parser')

        # Find the mini div elements on the page
        company_site_mini_divs_r = soup1.find_all('div', class_=['col-12 lg:col-6 mt-8 h-full lg:pr-3'])
        

        company_no = 0

        # Right first
        for mini_div_r in company_site_mini_divs_r:
            company_no = company_no + 1
            company_name_r = mini_div_r.find('p', class_='font-bold').text
            company_url_r = mini_div_r.find('a')['href']

            # Check if there is a project link
            if "developer-swasta" in company_url_r:
                project_no = 0
                response = requests.get(company_url_r)
                if response.status_code == 200:
                    soup2 = BeautifulSoup(response.text, 'html.parser')
                    project_site_mini_divs_r = soup2.find_all('div', class_=['col-12 md:col-6 pr-0 md:pr-3 mt-8'])
                    project_site_mini_divs_l = soup2.find_all('div', class_=['col-12 md:col-6 pl-0 md:pl-3 mt-8'])
                    # , 'col-12 md:col-6 pl-0 md:pl-3'
                    if project_site_mini_divs_r:
                        for micro_div_r in project_site_mini_divs_r:
                            # Find all mini div elements with the class "col-12 md:col-6" within the parent div
                            # Extract the <p class="font-bold"> element

                            # Right Side
                            project_location_element_r = micro_div_r.find('p', class_='font-bold').text.strip()
                            if project_location_element_r:
                                project_location_r = ' '.join(project_location_element_r.split())
                            # Extract the <a href=""> element
                            project_url_element_r = micro_div_r.find('a', href=True)
                            if project_url_element_r:
                                project_url_r = project_url_element_r['href']

                            project_no += 1
                            csv_writer.writerow([company_name_r, company_url_r, project_no, project_location_r, project_url_r])
                            print(f"{company_name_r} - project {project_no} scrapping COMPLETE")

                        if project_site_mini_divs_l:
                            for micro_div_l in project_site_mini_divs_l:
                                # Find all mini div elements with the class "col-12 md:col-6" within the parent div
                                # Extract the <p class="font-bold"> element

                                # Right Side
                                project_location_element_l = micro_div_l.find('p', class_='font-bold').text.strip()
                                if project_location_element_l:
                                    project_location_l = ' '.join(project_location_element_l.split())
                                # Extract the <a href=""> element
                                project_url_element_l = micro_div_l.find('a', href=True)
                                if project_url_element_l:
                                    project_url_l = project_url_element_l['href']

                                project_no += 1
                                csv_writer.writerow([company_name_r, company_url_r, project_no, project_location_l, project_url_l])
                                print(f"{company_name_r} - project {project_no} scrapping COMPLETE")


                    else:
                        null_project_location = 'NULL'
                        null_project_url = 'NULL'
                        csv_writer.writerow([company_name_r, company_url_r, project_no, null_project_location, null_project_url])
                        print(f"{company_name_r} - project {project_no} scrapping COMPLETE")

                    
                else:
                    print(f"Failed to retrieve page {page}. Status code: {response.status_code}")

                print(f"ALL PROJECTS OF - {company_name_r} - ARE EXTRACTED")

            else:
                print(f"There is an invalid URL in page {page} for company {company_no}")
                print("Please analyze the HTML and try again later")

        company_site_mini_divs_l = soup1.find_all('div', class_=['col-12 lg:col-6 mt-8 h-full lg:pl-3'])
        if company_site_mini_divs_l:
            for mini_div_l in company_site_mini_divs_l:
                company_no = company_no + 1
                company_name_l = mini_div_l.find('p', class_='font-bold').text
                company_url_l = mini_div_l.find('a')['href']

                # Check if there is a project link
                if "developer-swasta" in company_url_l:
                    project_no = 0
                    response = requests.get(company_url_l)
                    if response.status_code == 200:
                        soup2 = BeautifulSoup(response.text, 'html.parser')
                        project_site_mini_divs_r = soup2.find_all('div', class_=['col-12 md:col-6 pr-0 md:pr-3 mt-8'])
                        project_site_mini_divs_l = soup2.find_all('div', class_=['col-12 md:col-6 pl-0 md:pl-3 mt-8'])
                        # , 'col-12 md:col-6 pl-0 md:pl-3'
                        if project_site_mini_divs_r:
                            for micro_div_r in project_site_mini_divs_r:
                                # Find all mini div elements with the class "col-12 md:col-6" within the parent div
                                # Extract the <p class="font-bold"> element

                                # Right Side
                                project_location_element_r = micro_div_r.find('p', class_='font-bold').text.strip()
                                if project_location_element_r:
                                    project_location_r = ' '.join(project_location_element_r.split())
                                # Extract the <a href=""> element
                                project_url_element_r = micro_div_r.find('a', href=True)
                                if project_url_element_r:
                                    project_url_r = project_url_element_r['href']

                                project_no += 1
                                csv_writer.writerow([company_name_l, company_url_l, project_no, project_location_r, project_url_r])
                                print(f"{company_name_l} - project {project_no} scrapping COMPLETE")

                            if project_site_mini_divs_l:
                                for micro_div_l in project_site_mini_divs_l:
                                    # Find all mini div elements with the class "col-12 md:col-6" within the parent div
                                    # Extract the <p class="font-bold"> element

                                    # Right Side
                                    project_location_element_l = micro_div_l.find('p', class_='font-bold').text.strip()
                                    if project_location_element_l:
                                        project_location_l = ' '.join(project_location_element_l.split())
                                    # Extract the <a href=""> element
                                    project_url_element_l = micro_div_l.find('a', href=True)
                                    if project_url_element_l:
                                        project_url_l = project_url_element_l['href']

                                    project_no += 1
                                    csv_writer.writerow([company_name_l, company_url_l, project_no, project_location_l, project_url_l])
                                    print(f"{company_name_l} - project {project_no} scrapping COMPLETE")


                        else:
                            null_project_location = 'NULL'
                            null_project_url = 'NULL'
                            csv_writer.writerow([company_name_l, company_url_l, project_no, null_project_location, null_project_url])
                            print(f"{company_name_l} - project {project_no} scrapping COMPLETE")

                        
                    else:
                        print(f"Failed to retrieve page {page}. Status code: {response.status_code}")

                    print(f"ALL PROJECTS OF - {company_name_l} - ARE EXTRACTED")

                else:
                    print(f"There is an invalid URL in page {page} for company {company_no}")
                    print("Please analyze the HTML and try again later")



        print(f"Entire page {page} scrapping COMPLETE!!")


    else:
        print(f"Failed to retrieve page {page}. Status code: {response.status_code}")

print("Data extraction COMPLETED!!!")

# Close the CSV file
csv_file.close()
