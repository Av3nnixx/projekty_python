import time
import serial
import dhooks
embed = dhooks.embed.Embed(description="Uwazaj",
                           color= 0xcf0829,
                           timestamp= "now")
image1 = "https://example.com/icon.png"
embed.set_title("Ktos ruszyl sie w twoim domu")
embed.set_author(name="Autor", icon_url="https://example.com/icon.png")
embed.set_thumbnail("https://example.com/thumbnail.png")
embed.set_image("https://example.com/image.png")
embed.set_footer(text="Stopka", icon_url="https://example.com/footer.png")

embed.add_field(name="Godzina 1", value="Wartość 1", inline=True)
embed.add_field(name="Pole 2", value="Wartość 2", inline=True)
hook = dhooks.Webhook("https://discord.com/api/webhooks/1468932551556075677/FPVJuUDEwWKOuo6x88aO7NbFibY2L9cHxv8aAAFs78Uq23awTLCVuILeUpR3W5ykNzUE")
arduino = serial.Serial("COM7",9600,timeout=2)
time.sleep(2)
arduino.reset_input_buffer()
arduino.reset_output_buffer()
do_quit = False
def send_to_discord():
    pass
while not do_quit:
    received = arduino.readline().decode().strip()
    if received:
        hook.send(embed=embed)

