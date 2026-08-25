import pandas as pd

concrete_full = pd.read_csv('Concrete Compressive Strength.csv')

# Dropping Engineered Features and keeping Original Features
concrete = concrete_full.drop(columns = ['water_cement_ratio', 'total_binder', 'aggregate_to_cement', 'cement_water_interaction', 'age_strength_proxy'])

concrete.to_csv('concrete.csv', index=False)