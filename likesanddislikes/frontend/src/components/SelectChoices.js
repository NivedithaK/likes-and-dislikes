import { useState } from "react";
import {
	FormControl,
	FormLabel,
	FormErrorMessage,
	FormHelperText,
	Input,
	Button,
	Stack,
	Text,
} from "@chakra-ui/react";
import axios from "axios";

export default function SelectChoices(props) {
	const [like, setLike] = useState("");
	const [dislike, setDislike] = useState("");
	const [likeInputError, setLikeInputError] = useState("");
	const [dislikeInputError, setDislikeInputError] = useState("");
  let player_id = props.location.state.player_id;

	const handleSubmit = async function (event) {
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

		const headers = {
			"Content-Type": "application/json",
		};
		axios
			.post(
				`http://127.0.0.1:8000/likes-and-dislikes/set-like-dislike/`,
				{ player_id: player_id, like: like, dislike: dislike },
				{ headers }
			)
			.then((result) => {
				if (result.status === 201) {
          console.log("worked")
					// go to next page
				}
			});
	};

	return (
		<Stack maxWidth={500} margin="auto" marginTop={20} spacing={5}>
			<Text fontSize="4xl">
				Enter something you love and something you hate!
			</Text>

			<form onSubmit={handleSubmit}>
				<FormControl isInvalid={likeInputError}>
					<FormLabel htmlFor="like">One thing I like is...</FormLabel>
					<Input
						type="text"
						id="like"
						onChange={({ target }) => setLike(target.value.trim())}
					/>
					<FormErrorMessage>{likeInputError}</FormErrorMessage>
				</FormControl>
				<FormControl isInvalid={dislikeInputError}>
					<FormLabel htmlFor="dislike">
						One thing I dislike is...
					</FormLabel>
					<Input
						type="text"
						id="dislike"
						onChange={({ target }) =>
							setDislike(target.value.trim())
						}
					/>
					<FormErrorMessage>{dislikeInputError}</FormErrorMessage>
					<Button type="submit">Confirm</Button>
				</FormControl>
			</form>
		</Stack>
	);
}
