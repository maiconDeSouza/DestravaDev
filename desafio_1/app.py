import functions_for_data_extraction as data_extractor
import send_email as email_sender

def format_weather_report(
        current_temperature, 
        sky_condition, 
        first_day, 
        first_day_temperature, 
        second_day, 
        second_day_temperature, 
        third_day, 
        third_day_temperature):
    return (
        f"Bom dia!\n\n"
        f"Hoje, a temperatura atual em São Paulo é de {current_temperature}. O céu está {sky_condition}.\n\n"
        f"A previsão para os próximos dias é a seguinte:\n"
        f"- {first_day}: {first_day_temperature}\n"
        f"- {second_day}: {second_day_temperature}\n"
        f"- {third_day}: {third_day_temperature}\n\n"
        f"Tenha um excelente dia!"
    )

weather_website = "https://www.tempo.com/sao-paulo.htm"

current_temperature_xpath = "/html/body/main/div[2]/section/section[1]/div[1]/div[1]/span/span[2]/span[1]/span/span/span[1]"
sky_condition_xpath = "/html/body/main/div[2]/section/section[1]/div[1]/div[2]/a/span[2]/span[2]"

first_day_xpath = "/html/body/main/div[2]/section/section[2]/div/ul/li[2]/span/span[1]"
first_day_temperature_xpath = "/html/body/main/div[2]/section/section[2]/div/ul/li[2]/span/span[4]/span[1]"

second_day_xpath = "/html/body/main/div[2]/section/section[2]/div/ul/li[3]/span/span[1]"
second_day_temperature_xpath = "/html/body/main/div[2]/section/section[2]/div/ul/li[3]/span/span[4]/span[1]"

third_day_xpath = "/html/body/main/div[2]/section/section[2]/div/ul/li[4]/span/span[1]"
third_day_temperature_xpath = "/html/body/main/div[2]/section/section[2]/div/ul/li[4]/span/span[4]/span[1]"

data_extractor.navigate_to_the_website(weather_website)

current_temperature = data_extractor.extract_data("Current Temperature", current_temperature_xpath)
sky_condition = data_extractor.extract_data("Sky Condition", sky_condition_xpath)

first_day = data_extractor.extract_data("First Day", first_day_xpath)
first_day_temperature = data_extractor.extract_data("First Day Temperature", first_day_temperature_xpath)

second_day = data_extractor.extract_data("Second Day", second_day_xpath)
second_day_temperature = data_extractor.extract_data("Second Day Temperature", second_day_temperature_xpath)

third_day = data_extractor.extract_data("Third Day", third_day_xpath)
third_day_temperature = data_extractor.extract_data("Third Day Temperature", third_day_temperature_xpath)

data_extractor.quit_website()

weather_report = format_weather_report(
    current_temperature=current_temperature["Current Temperature"], 
    sky_condition=sky_condition["Sky Condition"], 
    first_day=first_day["First Day"], 
    first_day_temperature=first_day_temperature["First Day Temperature"], 
    second_day=second_day["Second Day"], 
    second_day_temperature=second_day_temperature["Second Day Temperature"], 
    third_day=third_day["Third Day"], 
    third_day_temperature=third_day_temperature["Third Day Temperature"]
)

email_sender.send_email(weather_report)
