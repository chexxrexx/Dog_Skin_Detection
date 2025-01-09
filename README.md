<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#demo">Demo</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The AI Dog Skin Detection Project addresses the issue of various dog skin diseases and the ability to let dog owners have some idea of what may be wrong with their dogs skin. 

For this project, 4 categories of dog skin disease were used:
* Healthy
* Bacterial dermatitis
* Fungal infection
* Hypersensitivity

Utilising META AI's DINOv2 and Pytorch, the AI has been trained over 1000 images of dog skin diseases and has an 80%+ accuracy in identifying which skin disease a dog may have. 

DISCLAIMER: As with all AI, it is not 100% accurate and therefore should not be used as a replacement for a professional veterinarian's diagnosis.

This project also won third place at the University of Edinburgh's AI Expo.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python]][Python-url]
* [![Pytorch][Pytorch]][Pytorch-url]
* [![DINOv2][DINOv2]][DINOv2-url]
* [![Streamlit][Streamlit]][Streamlit-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

Feel free to either install it yourself or look at our streamlit website made for our demo

### Prerequisites

It is advised that you view this code on google colab, otherwise a lot of libraries will have to be installed.

### Installation

1. Download the Model_Make.ipynb file
2. Open it using google colab
3. Run the code, it should save the model in a .pth file
4. Save the .pth file in your google drive
5. Replace the google drive url path in the web4.py file and run the file
6. Open the streamlit website that's formed

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Demo

https://dogskindetection2.streamlit.app/

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributors

Thank you to Arin06 for contributing to this project.

<!-- LICENSE -->
## License

Feel free to fork the project but PLEASE give credit.

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Read me template from: [OtherNeilDrew's github README.md](https://github.com/othneildrew/Best-README-Template/edit/main/README.md)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Pytorch]: https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white
[Pytorch-url]: https://pytorch.org/
[DINOv2]: https://img.shields.io/badge/Meta-0668E1?style=for-the-badge&logo=meta&logoColor=white
[DINOv2-url]: https://dinov2.metademolab.com/
[Streamlit]: https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white
[Streamlit-url]: https://streamlit.io/
