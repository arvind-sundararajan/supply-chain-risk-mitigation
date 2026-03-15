```json
{
    "tests/test_demand_forecasting.py": {
        "content": "
import logging
from typing import List, Dict
from pydantic_ai import StateGraph
from letta import MemoryManager
from giskard import NonStationaryDriftIndex
from biasalert import StochasticRegimeSwitch

logging.basicConfig(level=logging.INFO)

def test_demand_forecasting(non_stationary_drift_index: NonStationaryDriftIndex, 
                            stochastic_regime_switch: StochasticRegimeSwitch, 
                            memory_manager: MemoryManager) -> Dict:
    """
    Test demand forecasting with non-stationary drift index and stochastic regime switch.

    Args:
    - non_stationary_drift_index (NonStationaryDriftIndex): Non-stationary drift index.
    - stochastic_regime_switch (StochasticRegimeSwitch): Stochastic regime switch.
    - memory_manager (MemoryManager): Memory manager.

    Returns:
    - Dict: Test results.
    """
    try:
        # Initialize StateGraph
        state_graph = StateGraph()
        
        # Initialize memory manager
        memory_manager.initialize()
        
        # Calculate non-stationary drift index
        non_stationary_drift_index.calculate()
        
        # Apply stochastic regime switch
        stochastic_regime_switch.apply()
        
        # Forecast demand
        demand_forecast = state_graph.forecast()
        
        # Log results
        logging.info('Demand forecast: %s', demand_forecast)
        
        return {'demand_forecast': demand_forecast}
    except Exception as e:
        logging.error('Error: %s', e)
        return {'error': str(e)}

def test_rocket_science() -> None:
    """
    Test rocket science problem.

    Returns:
    - None
    """
    try:
        # Initialize non-stationary drift index
        non_stationary_drift_index = NonStationaryDriftIndex()
        
        # Initialize stochastic regime switch
        stochastic_regime_switch = StochasticRegimeSwitch()
        
        # Initialize memory manager
        memory_manager = MemoryManager()
        
        # Test demand forecasting
        test_demand_forecasting(non_stationary_drift_index, stochastic_regime_switch, memory_manager)
    except Exception as e:
        logging.error('Error: %s', e)

if __name__ == '__main__':
    test_rocket_science()
",
        "commit_message": "feat: implement specialized test_demand_forecasting logic"
    }
}
```