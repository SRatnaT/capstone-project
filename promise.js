
const fetchData = () => {

    const promise = new Promise((resolve , reject) => {
        setTimeout(() => {
         const success = false

         if(success){
            resolve("Data has been fetched")
         }else{
            reject("Data Fetching Error")
         }
        } , 2000)
    })

    return promise
}

fetchData()
.then((data) => console.log(data))
.catch((err) => console.log(err))