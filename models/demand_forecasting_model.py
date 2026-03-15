```json
{
    "models/demand_forecasting_model.py": {
        "content": "
import logging
from typing import List, Dict
from pydantic import BaseModel
from letta import MemoryManager
from giskard import StateGraph
from biasalert import BiasDetector

class DemandForecastingModel(BaseModel):
    """
    A model for forecasting demand in a supply chain.
    
    Attributes:
    non_stationary_drift_index (float): The index of non-stationary drift in the time series data.
    stochastic_regime_switch (bool): Whether to use stochastic regime switching in the model.
    """
    non_stationary_drift_index: float
    stochastic_regime_switch: bool

    def __init__(self, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """
        Initialize the demand forecasting model.
        
        Args:
        non_stationary_drift_index (float): The index of non-stationary drift in the time series data.
        stochastic_regime_switch (bool): Whether to use stochastic regime switching in the model.
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch
        self.memory_manager = MemoryManager()
        self.state_graph = StateGraph()
        self.bias_detector = BiasDetector()

    def fit(self, data: List[Dict]):
        """
        Fit the demand forecasting model to the given data.
        
        Args:
        data (List[Dict]): The data to fit the model to.
        
        Returns:
        None
        """
        try:
            logging.info('Fitting demand forecasting model')
            self.memory_manager.manage_memory()
            self.state_graph.build_state_graph(data)
            self.bias_detector.detect_bias(data)
        except Exception as e:
            logging.error(f'Error fitting demand forecasting model: {e}')

    def predict(self, data: List[Dict]) -> List[float]:
        """
        Make predictions using the demand forecasting model.
        
        Args:
        data (List[Dict]): The data to make predictions on.
        
        Returns:
        List[float]: The predicted values.
        """
        try:
            logging.info('Making predictions with demand forecasting model')
            predictions = self.state_graph.make_predictions(data)
            return predictions
        except Exception as e:
            logging.error(f'Error making predictions with demand forecasting model: {e}')

    def evaluate(self, data: List[Dict], predictions: List[float]) -> float:
        """
        Evaluate the performance of the demand forecasting model.
        
        Args:
        data (List[Dict]): The data to evaluate the model on.
        predictions (List[float]): The predicted values.
        
        Returns:
        float: The evaluation metric.
        """
        try:
            logging.info('Evaluating demand forecasting model')
            evaluation_metric = self.bias_detector.evaluate_predictions(data, predictions)
            return evaluation_metric
        except Exception as e:
            logging.error(f'Error evaluating demand forecasting model: {e}')

if __name__ == '__main__':
    # Simulation of the 'Rocket Science' problem
    data = [{'time': 1, 'value': 10}, {'time': 2, 'value': 20}, {'time': 3, 'value': 30}]
    model = DemandForecastingModel(non_stationary_drift_index=0.5, stochastic_regime_switch=True)
    model.fit(data)
    predictions = model.predict(data)
    evaluation_metric = model.evaluate(data, predictions)
    print(f'Predictions: {predictions}')
    print(f'Evaluation metric: {evaluation_metric}
",
        "commit_message": "feat: implement specialized demand_forecasting_model logic"
    }
}
```