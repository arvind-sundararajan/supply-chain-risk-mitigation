```json
{
    "utils/model_evaluator.py": {
        "content": "
import logging
from typing import Dict, List
from pydantic_ai import LangGraph
from letta import MemoryManager
from giskard import StochasticRegimeSwitch
from biasalert import BiasDetector

logging.basicConfig(level=logging.INFO)

class ModelEvaluator:
    def __init__(self, model_config: Dict):
        """
        Initialize the ModelEvaluator with a model configuration.

        Args:
        - model_config (Dict): A dictionary containing the model configuration.
        """
        self.model_config = model_config
        self.memory_manager = MemoryManager()
        self.lang_graph = LangGraph()
        self.stochastic_regime_switch = StochasticRegimeSwitch()
        self.bias_detector = BiasDetector()

    def evaluate_model(self, data: List) -> float:
        """
        Evaluate the model using the provided data.

        Args:
        - data (List): A list of data points to evaluate the model with.

        Returns:
        - float: The evaluation score of the model.
        """
        try:
            logging.info('Evaluating model...')
            self.lang_graph.build_state_graph()
            self.stochastic_regime_switch.apply_regime_switch()
            self.bias_detector.detect_bias()
            evaluation_score = self.memory_manager.calculate_memory_usage()
            logging.info('Model evaluation complete.')
            return evaluation_score
        except Exception as e:
            logging.error(f'Model evaluation failed: {e}')
            return None

    def calculate_non_stationary_drift_index(self, data: List) -> float:
        """
        Calculate the non-stationary drift index for the provided data.

        Args:
        - data (List): A list of data points to calculate the drift index for.

        Returns:
        - float: The non-stationary drift index of the data.
        """
        try:
            logging.info('Calculating non-stationary drift index...')
            drift_index = self.stochastic_regime_switch.calculate_drift_index(data)
            logging.info('Non-stationary drift index calculation complete.')
            return drift_index
        except Exception as e:
            logging.error(f'Non-stationary drift index calculation failed: {e}')
            return None

if __name__ == '__main__':
    # Simulate the 'Rocket Science' problem
    model_config = {
        'model_name': 'RocketScienceModel',
        'model_type': 'StochasticRegimeSwitch'
    }
    data = [1, 2, 3, 4, 5]
    model_evaluator = ModelEvaluator(model_config)
    evaluation_score = model_evaluator.evaluate_model(data)
    drift_index = model_evaluator.calculate_non_stationary_drift_index(data)
    logging.info(f'Model evaluation score: {evaluation_score}')
    logging.info(f'Non-stationary drift index: {drift_index}')
",
        "commit_message": "feat: implement specialized model_evaluator logic"
    }
}
```