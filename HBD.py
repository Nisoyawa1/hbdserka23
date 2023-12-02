import pandas as pd
from datetime import datetime, date, timedelta
import streamlit as st
import webbrowser
import openpyxl
from streamlit_option_menu import option_menu
from PIL import Image


with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Happy Birthday','WOF','PMS'], 
        icons=['house', 'list-task','list-task','list-task'], menu_icon="cast", default_index=1)
    selected

if selected=='Home':
    st.title('WELCOME to SERKA HMTM "PATRA" ITB KOMISARIAT PAGE')
    image=Image.open('serka.jpg')
    st.image(image, caption='inilah kami SERKA')


elif selected == 'Happy Birthday':
    st.title('HBD HMTM PATRA KOMISARIAT')
    st.header ('Ulang Tahun Hari Ini')
    #Read data
    df=pd.read_excel('HBD_20_21_22_FIX_1.xlsx',sheet_name='FIX')


    df=df[['NAMA','PATRA','PJ','Unique Code','Foto Diri']]
    df=df.applymap(str)

    # current dateTime
    now = datetime.now()

    # convert to string
    date_time_str_lst=[]
    date_time_str = now+ timedelta(days=0)
    date_time_str = date_time_str.strftime('%m%d').lstrip('0')
    df_new=df[df['Unique Code'].str.fullmatch(date_time_str)]


    #Using unique Code
    df_new=df[df['Unique Code'].str.fullmatch(date_time_str)]
    df_new_=df_new[['NAMA','PATRA','PJ','Foto Diri']]

    #FOR TOMMOROW 
    date_time_str_lst=[]
    date_time_str_next = now+ timedelta(days=1)
    date_time_str_next = date_time_str_next.strftime('%m%d').lstrip('0')
    df_new_1=df[df['Unique Code'].str.fullmatch(date_time_str_next)]
    
    #Using unique Code
    df_new_1=df[df['Unique Code'].str.fullmatch(date_time_str_next)]
    df_new_next=df_new_1[['NAMA','PATRA','PJ']]

    hide_dataframe_row_index = """
                <style>
                .row_heading.level0 {display:none}
                .blank {display:none}
                </style>
                """

    # Inject CSS with Markdown
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
    st.table(df_new_)


    st.header ('Ulang Tahun Besok')
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
    st.table(df_new_next)


    st.header ('Guide Line HBD')
    st.text('1. Buka google calendar dan atau lihat pembagian HBDan di web ini')
    st.text('2. Chat Tiara buat booking publikasi minimal J-3 ')
    st.text('3. Cek database, didalemnya yang perlu dicek: foto dan divisinya, download fotonya:')

    st.write( '[Taraksa Mahogra](https://drive.google.com/drive/folders/1k2bz8m01luw88IdfE1ryjpIKdWwnSQyxEkFFgK6TN2_7S_8q-gT1Ko4fNCygnlnLJbCZbLli)')
    st.write( '[Aquileo](https://drive.google.com/drive/folders/1mhpdPt4jmCbQuUPCLKTCV4637U2lRDdR2W3SJdvt2nIWRRV2y19XdljH1ukbpvKt5AnP4-3s)')

    st.write('4. Edit foto pake canva aja biar gampang, [ini linknya](https://www.canva.com/design/DAFpbr-v4lY/ZZJEjWNos6Hq4l2HU-lnNg/edit) ')
    st.text('    Login pake canva premium biar gampang editnya')
    st.text('    Uname: serkainternal@gmail.com')
    st.text('    Password: serka2022')
    st.write( '5. Terus buat fun factnya, tanya temen deketnya ya. ')
    st.write( 'Untuk Temen deketnya bisa dicari disini: [ini linknya](https://canva.com)')
    st.text(' Kalau gaada disini bisa chat gw aja atau ketang nya di masing masing angkatan')



elif selected == 'WOF':

    dict_WOF={
        'Nama':['Putri', 'Niso', 'Zuhdy', 'Najwa'],
        'Kuartal': ['Kuartal','Kuartal 2', 'Kuartal 3', 'Kuartal 4']
    }

    df_WOF=pd.DataFrame(dict_WOF)

    hide_dataframe_row_index = """
                <style>
                .row_heading.level0 {display:none}
                .blank {display:none}
                </style>
                """

    # Inject CSS with Markdown
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)


    st.title('WALL OF FAME PATRA')
    st.table(df_WOF)
    st.text('1. Lihat link nya disini')
    st.write( '[WOF LINK]()')
    st.text('2. Buat dan masukkan Nama nama dari link diatas')
    st.text('FOTO FOTO ANGKATAN')
    st.write( '[Taraksa Mahogra](https://drive.google.com/drive/folders/1k2bz8m01luw88IdfE1ryjpIKdWwnSQyxEkFFgK6TN2_7S_8q-gT1Ko4fNCygnlnLJbCZbLli)')
    st.write( '[Aquileo](https://drive.google.com/drive/folders/1mhpdPt4jmCbQuUPCLKTCV4637U2lRDdR2W3SJdvt2nIWRRV2y19XdljH1ukbpvKt5AnP4-3s)')
    st.text('2. Masukkan Data data diatas kedalam link canva dibawah')
    st.write( '[WOF LINK CANVA POST](https://www.canva.com/design/DAFsMI_hA8s/zG2HkGza0rfjOXcY6AFgMA/edit)')
    st.write( '[WOF LINK CANVA PRINT](https://www.canva.com/design/DAFt0DiVXEs/xQSWMnG0-P2H90pWb10-Gw/edit)')
    st.write('3. Untuk Publikasi chat ke Tiara yaa')

elif selected =='PMS':
    st.title('WALL OF FAME PATRA')
    import pandas as pd
    from datetime import datetime, timedelta

    # Assuming you have imported streamlit as st and have set up the 'df_pms' DataFrame

    # Read Excel file
    df_pms = pd.read_excel('Pembagian.xlsx')

    # Current dateTime
    now = datetime.now()
    # Convert to string
    date_time_str = (now + timedelta(days=0)).strftime('%m%d').lstrip('0')

    # Convert 'Unique Code' column to string
    df_pms['Unique Code'] = df_pms['Unique Code'].astype(str)

    # Filter the DataFrame using str.fullmatch()
    df_new_pms = df_pms[df_pms['Unique Code'].str.fullmatch(date_time_str)]

    # Display the filtered DataFrame
    st.write(df_new_pms)

    hide_dataframe_row_index = """
                <style>
                .row_heading.level0 {display:none}
                .blank {display:none}
                </style>
                """

    # Inject CSS with Markdown
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

    st.title( 'Guideline')
    st.write( '[Link Google Drive](https://bit.ly/PATRAMudaShowcase)')
    st.write('Caption')
    st.write('𝗣𝗔𝗧𝗥𝗔 𝗠𝗨𝗗𝗔 𝗦𝗛𝗢𝗪𝗖𝗔𝗦𝗘')
    st.write('Haiii massa Komisariat HMTM ""PATRA"" ITB 🙌')
    st.write("Berhubung kemarin PATRA '22 telah membuat video perkenalan 🤩 berikut merupakan video perkenalan oleh:")
    st.write("1. Muhammad Reza Muhtadi (PATRA222113)")
    st.write("2. Fadli Ahmad Fadillah (PATRA222114)")
    st.write("Raka pakai bikini 😲 Sambil berjemur di arab dan phukat 🤔 Semoga melalui video ini ☺️ Kita semua jadi lebih akrab dan dekat 😉")
    st.write("~~ 𝘴𝘦𝘭𝘢𝘮𝘢𝘵 𝘮𝘦𝘯𝘰𝘯𝘵𝘰𝘯  ~~")
    st.write("Uji coba terlebih dahulu bot : //PATRAMudaShowcase pada grup Cerelation")

    st.write('Kalau susah copy caption silakan buka notes grup')
    

  
    
