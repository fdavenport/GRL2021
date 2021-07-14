## ----------------------------------------------------------------------------
from tensorflow.keras import models, layers
from tensorflow.keras import metrics 
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import regularizers

class MulticlassAUC(metrics.AUC):
    """AUC for a single class in a muliticlass problem.

    Parameters
    ----------
    pos_label : int
        Label of the positive class (the one whose AUC is being computed).

    from_logits : bool, optional (default: False)
        If True, assume predictions are not standardized to be between 0 and 1.
        In this case, predictions will be squeezed into probabilities using the
        softmax function.

    sparse : bool, optional (default: True)
        If True, ground truth labels should be encoded as integer indices in the
        range [0, n_classes-1]. Otherwise, ground truth labels should be one-hot
        encoded indicator vectors (with a 1 in the true label position and 0
        elsewhere).

    **kwargs : keyword arguments
        Keyword arguments for tf.keras.metrics.AUC.__init__(). For example, the
        curve type (curve='ROC' or curve='PR').
    """

    def __init__(self, pos_label, from_logits=False, sparse=True, **kwargs):
        super().__init__(**kwargs)

        self.pos_label = pos_label
        self.from_logits = from_logits
        self.sparse = sparse

    def update_state(self, y_true, y_pred, **kwargs):
        """Accumulates confusion matrix statistics.

        Parameters
        ----------
        y_true : tf.Tensor
            The ground truth values. Either an integer tensor of shape
            (n_examples,) (if sparse=True) or a one-hot tensor of shape
            (n_examples, n_classes) (if sparse=False).

        y_pred : tf.Tensor
            The predicted values, a tensor of shape (n_examples, n_classes).

        **kwargs : keyword arguments
            Extra keyword arguments for tf.keras.metrics.AUC.update_state
            (e.g., sample_weight).
        """
        if self.sparse:
            y_true = tf.math.equal(y_true, self.pos_label)
            y_true = tf.squeeze(y_true)
        else:
            y_true = y_true[..., self.pos_label]

        if self.from_logits:
            y_pred = tf.nn.softmax(y_pred, axis=-1)
        y_pred = y_pred[..., self.pos_label]

        super().update_state(y_true, y_pred, **kwargs)

METRICS = [
    metrics.CategoricalAccuracy(name='accuracy'),
    metrics.Precision(class_id = 1, name='precision'),
    metrics.Recall(class_id = 1, name='recall'),
    MulticlassAUC(pos_label = 1, sparse = False, name = 'auc')
]

def build_model(lr = .0004, conv_filters = 16, dense_neurons = 16, dense_layers = 1, 
                activity_reg = 0.001, dropout_rate = 0.2, input_channels = 2):

    model = models.Sequential() 
    model.add(layers.Input(shape=(15, 35, input_channels))) ## define input shape
    
    model.add(layers.Conv2D(conv_filters, 
                            (3,3), activity_regularizer=regularizers.l2(0.01))) 
    model.add(layers.Activation('relu')) ## add convolutional layer
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Dropout(dropout_rate))
                            
    model.add(layers.Conv2D(conv_filters, (3,3), activity_regularizer=regularizers.l2(activity_reg))) 
    model.add(layers.Activation('relu')) ## add convolutional layer
    model.add(layers.MaxPooling2D((2,2))) ## pooling layer
    model.add(layers.Dropout(dropout_rate))
                            
    model.add(layers.Flatten()) ## converts from 2D array to 1D array
    
    for i in range(dense_layers):
        model.add(layers.Dense(dense_neurons, activity_regularizer=regularizers.l2(activity_reg))) ## dense layer
        model.add(layers.Activation('relu'))
     
    model.add(layers.Dense(2, activation='softmax')) ## classifier layer (binary class where 1=extreme)
    
    model.compile(loss=losses.CategoricalCrossentropy(), 
                  optimizer=optimizers.Adam(learning_rate = lr), 
                  metrics=METRICS)
    return(model)
