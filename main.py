import streamlit as st 
import pandas as pd
import api.api as api

def showData(data):
  return

st.set_page_config("Projeto validade")

st.title("Projeto validade")

if __name__ == "__main__":
    # Começo da tela
       itensParaVencer, adicionar = st.tabs(['Itens para vencer', 'Adicionar Item'])
        
       with itensParaVencer:
            itensParaVencer.dataframe(pd.json_normalize(api.getAllItens()),
                                    column_config={
                                         "name" : "Nome",
                                         "dtValid" : "Data de Validade",
                                         "inEstoque" : "Tem no Estoque"
                                    },  
                                      hide_index=True,)
          #  itensParaVencer.table()
       # with adicionar:
        #     adicionar.subheader('Adicionar item')
             
             