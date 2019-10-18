<template>
    <div id="app">
        <b-container>
            <b-row>
                <b-col align-self="center">
                    <b-jumbotron header="Aprendizado Supervisionado">
                        <p class="mt-5">Informações no <a
                                href="https://github.com/pablozandona/medical-appointment-classifier">repositório</a>.
                        </p>
                    </b-jumbotron>
                </b-col>
                <b-col  align-self="center">
                    <Form msg="Welcome to Your Vue.js App"/>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
    import Form from './components/Form.vue'

    import 'bootstrap/dist/css/bootstrap.css'
    import 'bootstrap-vue/dist/bootstrap-vue.css'

    import Vue from 'vue'
    import BootstrapVue from 'bootstrap-vue'

    Vue.use(BootstrapVue);

    export default {
        name: 'app',
        components: {
            Form
        }
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
