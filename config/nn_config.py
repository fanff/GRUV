def get_neural_net_configuration():
	nn_params = {}
	nn_params['sampling_frequency'] = 44100
	#Number of hidden dimensions.
	#For best results, this should be >= freq_space_dims, but most consumer GPUs can't handle large sizes
	nn_params['hidden_dimension_size'] = 64



	nn_params['num_iters'] = 20
	nn_params['epochs_per_iter'] = 2


	nn_params['work_folder'] = './datasets'
	#The weights filename for saving/loading trained models
	nn_params['model_basename'] = './datasets/YourMusicLibraryNPWeights'
	#The model filename for the training data
	nn_params['model_file'] = './datasets/YourMusicLibraryNP'
	#The dataset directory
	nn_params['dataset_directory'] = './datasets/YourMusicLibrary/'
	return nn_params
