import { useState } from "react";
import {
	FormControl,
	FormLabel,
	FormErrorMessage,
	FormHelperText,
	Input,
	Button,
	Stack,
	Text
} from "@chakra-ui/react";

export default function SelectChoices(props) {

  const [like, setLike] = useState("");
  const [dislike, setDislike] = useState("");
  const [likeInputError, setLikeInputError] = useState("");
  const [dislikeInputError, setDislikeInputError] = useState("");

  const url = "";


  const handleSubmit = async function(event) {
    event.preventDefault();
    let hasError = false;

    if (like === "") {
      setLikeInputError("This field is required");
      hasError = true;
    } else {
      setLikeInputError("");
    }

    if (dislike === "") {
      setDislikeInputError("This field is required");
      hasError = true;
    } else {
      setDislikeInputError("");
    }

    if (hasError) {
      return;
    }

    const res = await fetch(`${url}/set-likes-dislikes`, {
      method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ playerId: null, likes: like, dislikes: dislike })
    });

    if (res.status === 200) {
      //transition into next page
    }


  }

  return (
    <Stack maxWidth={500} margin="auto" marginTop={20} spacing={5}>
      <Text fontSize="4xl">Enter something you love and something you hate!</Text>

      <form onSubmit={handleSubmit}>
        <FormControl isInvalid={likeInputError}>
          <FormLabel htmlFor="like">One thing I like is...</FormLabel>
          <Input
            type="text"
            id="like"
            onChange={({ target }) => setLike(target.value.trim())}
          />
          <FormErrorMessage>
            {likeInputError}
          </FormErrorMessage>
        </FormControl>
        <FormControl isInvalid={dislikeInputError}>
          <FormLabel htmlFor="dislike">One thing I dislike is...</FormLabel>
          <Input
            type="text"
            id="dislike"
            onChange={({ target }) => setDislike(target.value.trim())}
          />
          <FormErrorMessage>
            {dislikeInputError}
          </FormErrorMessage>
          <Button type="submit">
            Confirm
          </Button>

        </FormControl>
      </form>
    </Stack>
  )
}