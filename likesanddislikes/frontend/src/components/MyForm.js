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
import React, { useState } from 'react';

const url = "";

export default function MyForm(props) {
	const [roomCode, setRoomCode] = useState("");
	const [name, setName] = useState("");
	const [roomError, setRoomError] = useState("");
	const [nameError, setNameError] = useState("");

	const handleSubmit = async function (event) {
		event.preventDefault();
		let hasError = false;
		if (roomCode.trim() === "") {
			setRoomError("You must set the room code if you are trying to join a game");
			hasError = true;
		} else {
			setRoomError("");
		}

		if (name.trim() === "") {
			setNameError("Name cannot be empty");
			hasError = true;
		} else {
			setNameError("");
		}

		if (hasError) {
			return;
		}

		const res = await fetch(`${url}/join-room`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ name })
		})
		if (res.status === 200) {
			let data = await res.json();
			const path = "/" + roomCode + "/waiting";
			props.history.push(path, { players_in_lobby: data.players_in_lobby });
		}
		const path = "/" + roomCode + "/waiting";
		props.history.push(path);
	}

	const createNewRoom = async function (event) {
		event.preventDefault();
		if (name.trim() === "") {
			setNameError("Name cannot be empty");
			return;
		} else {
			setNameError("");
		}

		const res = await fetch(`${url}/create-lobby-and-host`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ nickname: name })
		})
		if (res.status === 200) {
			let data = await res.json();
			let lobbyId = data.lobby_code;
			const path = "/" + lobbyId + "/waiting";
			props.history.push(path.anchor, { players_in_lobby: data.players_in_lobby });
		}
	}

	return (
		<Stack maxWidth={500} margin="auto" marginTop={20} spacing={5}>
			<Text fontSize="4xl">Likes and Dislikes</Text>

			<form onSubmit={handleSubmit}>
				<FormControl isInvalid={roomError}>
					<FormLabel htmlFor="room-code">Room code</FormLabel>
					<Input
						type="text"
						id="roomCode"
						onChange={({ target }) => setRoomCode(target.value.trim())}
					/>
					<FormErrorMessage>
						{roomError}
					</FormErrorMessage>
				</FormControl>
				<FormControl isInvalid={nameError}>
					<FormLabel htmlFor="name">Name</FormLabel>
					<Input
						type="text"
						id="name"
						onChange={({ target }) => setName(target.value)}
					/>
					<FormErrorMessage>
						{nameError}
					</FormErrorMessage>

					<Stack spacing={3} marginTop={10} align="center">
						<Button type="submit">
							Enter
						</Button>
						<Button onClick={createNewRoom}>
							Make a new room
						</Button>
					</Stack>
				</FormControl>
			</form>
		</Stack>
	)
}