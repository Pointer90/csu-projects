import * as THREE from 'three';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader'

//Требуемые переменные и константы
let logo = null,                                              //Хранилище логотипа
    canvas = document.querySelector("#preview");              //Канвас со спиралью

const sizes = {
    width: canvas.offsetWidth / 3,
    height: canvas.offsetHeight / 1.5,
};

//Создаём сцену с "бесконечным" пространством
const scene = new THREE.Scene();

//Создаём камеру типа Перспектива с FOV 75 и 500/500
const camera = new THREE.PerspectiveCamera(75, sizes.width / sizes.height, 0.1, 1000);
camera.position.set(0.2, 0, 3);
scene.add(camera);

//Создаём отрисовщика с прозрачным фоном и сглаженными краями
const renderer = new THREE.WebGLRenderer();
renderer.setSize(sizes.width, sizes.height);
renderer.setClearColor(0x000000, 0);
renderer.domElement.setAttribute("id", "CSULogo");
canvas.insertBefore(renderer.domElement, canvas.firstChild);

//Создаём пространственный свет
const aLight = new THREE.AmbientLight(0xeeeeee, 3);
scene.add(aLight);

//Создаём точечный свет
const pLight = new THREE.PointLight(0xffffff, 10);
pLight.position.set(1, 1, 2);
scene.add(pLight);

//Создаём загрузчик и запускаем функцию загрузги 
const loader = new GLTFLoader();
loader.load(
    "/static/src/models/CSU.gltf",
    (gltf) => {
        logo = gltf.scene.children[0];
        logo.scale.set(2, 2, 2);
        scene.add(logo);
    }
);
//Создаём функцию анимации
const clock = new THREE.Clock();

renderer.render(scene, camera);

function tick(){
    const elapsedTime = clock.getElapsedTime();
    if (logo){
        logo.rotation.y = elapsedTime;
    }
    renderer.render(scene, camera);
    window.requestAnimationFrame(tick);
};
tick();

// Базовые обработчики событий для поддержки ресайза
window.addEventListener('resize', () => {
// Обновляем размеры
canvas = document.querySelector("#preview");
sizes.width = canvas.offsetWidth / 3;
sizes.height = canvas.offsetHeight / 1.5;

// Обновляем соотношение сторон камеры
camera.aspect = sizes.width / sizes.height;
camera.updateProjectionMatrix();

// 	// Обновляем renderer
renderer.setSize(sizes.width, sizes.height);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 3));
renderer.render(scene, camera);
});