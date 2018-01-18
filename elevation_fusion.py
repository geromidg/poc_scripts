class Gaussian:
    def __init__(self, mean, variance):
        self.mean = mean
        self.variance = variance

def fuse(prior, measurement):
    innovation = measurement.mean - prior.mean
    gain = prior.variance / (prior.variance + measurement.variance)

    prior.mean += gain * innovation
    prior.variance *= 1.0 - gain

def compare(mean, variance, cloud_mean, cloud_variance):
    elevation = Gaussian(mean, variance)
    cloud = [Gaussian(m, cloud_variance) for m in cloud_mean]

    ### Fusion ###
    fusion_elevation = Gaussian(mean, variance)

    for point in cloud:
        fuse(fusion_elevation, point)

    print('Fusion')
    print(fusion_elevation.mean)
    print(fusion_elevation.variance)

    ### Average ###
    average_elevation = Gaussian(mean, variance)

    average_mean = 0.0
    for point in cloud:
        average_mean += point.mean
    average_mean /= len(cloud)

    fuse(average_elevation, Gaussian(average_mean, cloud_variance))

    print('Average')
    print(average_elevation.mean)
    print(average_elevation.variance)

if __name__ == '__main__':
    compare(1.5, 1.0, [3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9], 0.1)

