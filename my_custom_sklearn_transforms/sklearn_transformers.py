from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

 # removendo os outliers
class Remover_Outliers(BaseEstimator, TransformerMixin):
    def __init__(self):
        return

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        df = X.copy()    
        distance = 1.5 * (np.percentile(df['H_AULA_PRES'], 75) - np.percentile(df['H_AULA_PRES'], 25))
        df.drop(df[df['H_AULA_PRES'] > distance + np.percentile(df['H_AULA_PRES'], 75)].index, inplace=True)
        df.drop(df[df['H_AULA_PRES'] < np.percentile(df['H_AULA_PRES'], 25) - distance].index, inplace=True)
        return df

       
    

