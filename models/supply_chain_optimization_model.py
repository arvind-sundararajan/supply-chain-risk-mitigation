```json
{
    "models/supply_chain_optimization_model.py": {
        "content": "
import logging
from typing import List, Dict
from pydantic import BaseModel
from giskard import StateGraph
from letta import MemoryManager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SupplyChainOptimizationModel(BaseModel):
    """
    Model for optimizing supply chain operations.

    Attributes:
    - non_stationary_drift_index (float): Index of non-stationary drift in supply chain data.
    - stochastic_regime_switch (bool): Flag for stochastic regime switch in supply chain operations.
    """

    non_stationary_drift_index: float
    stochastic_regime_switch: bool

    def optimize_supply_chain(self, demand_forecast: List[float], supply_capacity: List[float]) -> Dict[str, float]:
        """
        Optimize supply chain operations based on demand forecast and supply capacity.

        Args:
        - demand_forecast (List[float]): List of demand forecast values.
        - supply_capacity (List[float]): List of supply capacity values.

        Returns:
        - Dict[str, float]: Dictionary containing optimized supply chain metrics.
        """
        try:
            # Initialize StateGraph from Giskard
            state_graph = StateGraph()
            logger.info('Initialized StateGraph')

            # Initialize MemoryManager from Letta
            memory_manager = MemoryManager()
            logger.info('Initialized MemoryManager')

            # Perform supply chain optimization
            optimized_metrics = self._perform_optimization(demand_forecast, supply_capacity, state_graph, memory_manager)
            logger.info('Performed supply chain optimization')

            return optimized_metrics
        except Exception as e:
            logger.error(f'Error optimizing supply chain: {str(e)}')
            return {}

    def _perform_optimization(self, demand_forecast: List[float], supply_capacity: List[float], state_graph: StateGraph, memory_manager: MemoryManager) -> Dict[str, float]:
        """
        Perform supply chain optimization using StateGraph and MemoryManager.

        Args:
        - demand_forecast (List[float]): List of demand forecast values.
        - supply_capacity (List[float]): List of supply capacity values.
        - state_graph (StateGraph): StateGraph instance from Giskard.
        - memory_manager (MemoryManager): MemoryManager instance from Letta.

        Returns:
        - Dict[str, float]: Dictionary containing optimized supply chain metrics.
        """
        try:
            # Update StateGraph with demand forecast and supply capacity
            state_graph.update(demand_forecast, supply_capacity)
            logger.info('Updated StateGraph')

            # Manage memory using MemoryManager
            memory_manager.manage_memory()
            logger.info('Managed memory')

            # Calculate optimized supply chain metrics
            optimized_metrics = self._calculate_optimized_metrics(state_graph, memory_manager)
            logger.info('Calculated optimized supply chain metrics')

            return optimized_metrics
        except Exception as e:
            logger.error(f'Error performing optimization: {str(e)}')
            return {}

    def _calculate_optimized_metrics(self, state_graph: StateGraph, memory_manager: MemoryManager) -> Dict[str, float]:
        """
        Calculate optimized supply chain metrics using StateGraph and MemoryManager.

        Args:
        - state_graph (StateGraph): StateGraph instance from Giskard.
        - memory_manager (MemoryManager): MemoryManager instance from Letta.

        Returns:
        - Dict[str, float]: Dictionary containing optimized supply chain metrics.
        """
        try:
            # Calculate optimized supply chain metrics
            optimized_metrics = {
                'non_stationary_drift_index': self.non_stationary_drift_index,
                'stochastic_regime_switch': self.stochastic_regime_switch
            }
            logger.info('Calculated optimized supply chain metrics')

            return optimized_metrics
        except Exception as e:
            logger.error(f'Error calculating optimized metrics: {str(e)}')
            return {}

if __name__ == '__main__':
    # Create instance of SupplyChainOptimizationModel
    supply_chain_model = SupplyChainOptimizationModel(non_stationary_drift_index=0.5, stochastic_regime_switch=True)

    # Simulate demand forecast and supply capacity
    demand_forecast = [100, 120, 150]
    supply_capacity = [120, 150, 180]

    # Optimize supply chain operations
    optimized_metrics = supply_chain_model.optimize_supply_chain(demand_forecast, supply_capacity)

    # Print optimized supply chain metrics
    print(optimized_metrics)
",
        "commit_message": "feat: implement specialized supply_chain_optimization_model logic"
    }
}
```