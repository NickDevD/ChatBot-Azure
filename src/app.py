import streamlit as st


def configure_interface():
    st.title("Upload de Arquivos DIO - Azure")
    uploaded_file = st.file_uploader("Escolha um Arquivo", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        blob_url =""
        if blob_url:
            st.write(f"Arquivo {fileName} enviado com sucesso para o Azure Blob Storage")
            credit_card_info = ""
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo {fileName} para o Azure Blob Storage")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada", use_column_width=True)
    st.write("informações do cartão de credito encontradas:")
    st.write(credit_card_info)





if __name__=="__main__":
    configure_interface()

