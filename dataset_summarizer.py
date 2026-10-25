class DatasetSummarizer:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def generar_resumen(self, nombre_archivo="resumen_dataset.txt"):
        df = self.dataframe

        print("Generando resumen...")

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("RESUMEN DEL DATASET\n")
            archivo.write("===================\n\n")

            archivo.write(f"Cantidad de filas: {df.shape[0]}\n")
            archivo.write(f"Cantidad de columnas: {df.shape[1]}\n\n")

            archivo.write("NOMBRES Y TIPOS DE COLUMNAS\n")
            archivo.write("---------------------------\n")

            for columna in df.columns:
                archivo.write(f"{columna}: {df[columna].dtype}\n")

            archivo.write("\nVALORES NULOS POR COLUMNA\n")
            archivo.write("------------------------\n")
            archivo.write(df.isnull().sum().to_string())

            archivo.write("\n\nESTADISTICAS DESCRIPTIVAS\n")
            archivo.write("-------------------------\n")
            archivo.write(df.describe().to_string())

        print(f"Resumen guardado en: {nombre_archivo}")
