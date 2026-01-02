
// const fetchData = () => {

//     return new Promise((resolve, reject) => {

//         setTimeout(() => {

//             const success = false

//             if (success) {

//                 resolve("Async await data fetched success")

//             } else (
//                 reject("Async await data fetch error")
//             )

//         }, 2000)

//     })
// }


// async function getData() {
//     try {
//         const result = await fetchData();
//         console.log(result);

//     } catch (err) {

//         console.log(err);


//     }

// }

// getData()


const fetchData = () => {

    return new Promise((resolve, reject) => {
        setTimeout(() => {

            const success = true

            if (success) {
                resolve("Async await success")
            } else {
                reject("Asybc await failure")
            }

        }, 2000)
    })
}

const getData = async () => {

    try {
        const result = await fetchData()
        console.log(result);

    } catch(err) {

        console.error(err)

    }

}

getData()