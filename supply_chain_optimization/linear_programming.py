```json
{
    "supply_chain_optimization/linear_programming.py": {
        "content": "
import logging
from typing import List, Dict
from pydantic import BaseModel
from giskard import StateGraph
from letta import MemoryManager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SupplyChainOptimization(BaseModel):
    """Represents a supply chain optimization problem."""
    non_stationary_drift_index: float
    stochastic_regime_switch: bool

    def solve(self) -> Dict:
        """Solves the supply chain optimization problem using linear programming."""
        try:
            # Create a StateGraph to model the supply chain
            graph = StateGraph()
            graph.add_node('warehouse')
            graph.add_node('distribution_center')
            graph.add_edge('warehouse', 'distribution_center')

            # Define the objective function and constraints
            objective = 'minimize'
            constraints = [
                'non_stationary_drift_index <= 0.5',
                'stochastic_regime_switch == True'
            ]

            # Solve the linear programming problem
            solution = graph.solve(objective, constraints)
            logger.info('Solution found: %s', solution)
            return solution
        except Exception as e:
            logger.error('Error solving supply chain optimization problem: %s', e)
            return {}

    def optimize(self, memory_manager: MemoryManager) -> List:
        """Optimizes the supply chain using the given memory manager."""
        try:
            # Use the memory manager to optimize the supply chain
            optimized_supply_chain = memory_manager.optimize(self)
            logger.info('Optimized supply chain: %s', optimized_supply_chain)
            return optimized_supply_chain
        except Exception as e:
            logger.error('Error optimizing supply chain: %s', e)
            return []

def main():
    # Create a SupplyChainOptimization instance
    optimization = SupplyChainOptimization(non_stationary_drift_index=0.3, stochastic_regime_switch=True)

    # Solve the supply chain optimization problem
    solution = optimization.solve()
    print('Solution:', solution)

    # Optimize the supply chain using a memory manager
    memory_manager = MemoryManager()
    optimized_supply_chain = optimization.optimize(memory_manager)
    print('Optimized supply chain:', optimized_supply_chain)

if __name__ == '__main__':
    main()
        ",
        "commit_message": "feat: implement specialized linear_programming logic"
    }
}
```