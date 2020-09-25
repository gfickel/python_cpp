#include "contrast_image.h"

void cpp_contrast_image(const unsigned char *image, int height, int width, unsigned char *outResult) {
    auto vec = std::vector<unsigned char>(image, image+width*height);
    auto minmax = std::minmax_element(vec.begin(), vec.end());
    float min = (float)*minmax.first;
    float max = (float)*minmax.second;
    float delta_color = max-min;
    for (int row=0; row<height; row++) {
        for (int col=0; col<width; col++) {
            int idx = row*width + col;
            float pixel = (float)image[idx];
            outResult[idx] = (unsigned char)(255*(pixel-min)/delta_color);
        }
    }
}
