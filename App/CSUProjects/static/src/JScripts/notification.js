// const toastLiveExample = document.getElementById('liveToast')
// const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
// toastBootstrap.show()

function notify(){
    const tag = document.getElementById('notify')
    const notify = bootstrap.Toast.getOrCreateInstance(tag)

    notify.show()
}

notify()