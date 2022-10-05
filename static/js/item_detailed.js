const addToFavourite = async ({ item }) => {
  const favouriteButton = document.getElementById(`${item}-favourite`)
  const favouriteIcon = document.getElementById(`${item}-favorite-icon`)
  try {
    const response = await fetch(`/favorite-item/${item}`, { method: "GET" })
    const data = await response.json()
    console.log(data)
    if (response.status == 400) {
      alert(data)
      return
    }
    favouriteButton.className = data.fav_class
    favouriteIcon.className = data.icon_class
  } catch (error) {
    console.error(error)
  }
}

const addToWishList = async ({ item }) => {
  const checkInput = document.getElementById(`${item}-is-wishlist`)
  try {
    const response = await fetch(`/wishlist-item/${item}`, { method: "GET" })
    const data = await response.json()
    console.log(data)
    if (response.status == 400) {
      alert(data)
      return
    }
    checkInput.checked = data.is_wishlist
  } catch (error) {
    console.error(error)
  }
}
