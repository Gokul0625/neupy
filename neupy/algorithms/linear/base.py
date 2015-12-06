from neupy.utils import is_list_of_integers
from neupy.layers.connections import NetworkConnectionError, LayerConnection
from neupy.network import SupervisedConstructableNetwork
from neupy.layers import Step, Output


__all__ = ('BaseLinearNetwork',)


class BaseLinearNetwork(SupervisedConstructableNetwork):
    """ Base class for feedforward neural network without hidden layers.

    Notes
    -----
    * Input layer should be :layer:`Step` class instance.

    Parameters
    ----------
    {linear_connection}
    {full_params}

    Methods
    -------
    {plot_errors}
    {last_error}
    """

    shared_docs = {"linear_connection": """connection : list, tuple or object
        Should be a list or tuple that contains two integers. First integer
        describe number of input units and the seconds one number of output
        units.
    """}

    def __init__(self, connection, **options):
        if len(connection) != 2:
            raise ValueError("This network should contains two layers.")

        if is_list_of_integers(connection):
            input_layer_size, output_layer_size = connection
            connection = Step(input_layer_size) > Output(output_layer_size)

        if not isinstance(connection, LayerConnection):
            raise ValueError("Invalid network connection structure.")

        if not isinstance(connection.input_layer, Step):
            raise NetworkConnectionError(
                "Input layer should contains step activation function "
                "(``Step`` class instance)."
            )

        super(BaseLinearNetwork, self).__init__(connection, **options)
