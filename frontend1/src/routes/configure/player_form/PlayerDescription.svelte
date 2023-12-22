<script>
    import Age from "./Age.svelte";
    import Select from "./Select.svelte";

    export let player_info = {
        name: "",
        age: 1,
        hair_color: "",
        energy: "",
        role: "",
        aptitude: "",
        humor: "",
    };
</script>

<div>
    <p>Agent name</p>
    <input type="text" bind:value={player_info.name} placeholder="Agent name" />
    <p>How old is your agent?</p>
    <div class="button-container">
        <Age bind:age={player_info.age} />
    </div>
    <p>Hair color</p>
    <div class="button-container">
        <Select
            bind:selected={player_info.hair_color}
            options={["black", "brown", "blond", "white/gray", "rarely red"]}
        />
    </div>
    <p>Choose the communication type of your player</p>
    <div class="button-container">
        <Select
            bind:selected={player_info.energy}
            options={["Assertive", "Passive", "Aggressive", "Manipulative"]}
        />
    </div>

    <p>How do you define your player?</p>
    <div class="button-container">
        <Select
            bind:selected={player_info.role}
            options={["Leader", "Follower"]}
        />
    </div>
    <p>Choose your player's sense of humor</p>
    <div class="button-container">
        <Select
            bind:selected={player_info.humor}
            options={["Ironical", "Absurd", "Neutral", "Serious"]}
        />
    </div>

    <p>Choose the main skill or ability</p>
    <div class="button-container">
        <Select
            bind:selected={player_info.aptitude}
            options={["Sceptical", "Open-minded", "Intolerant", "Tolerant"]}
        />
    </div>
</div>

<style>
    .button-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
</style>
