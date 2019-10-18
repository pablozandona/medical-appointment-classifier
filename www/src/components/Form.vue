<template>
    <div>
        <b-form @submit="onSubmit" @reset="onReset" v-if="show">
            <b-form-group
                    label="Data do agendamento:"
                    label-for="input-1"
                    label-cols-lg="6"
                    label-align="right"
            >
                <b-form-input
                        id="input-1"
                        v-model="form.data_agendamento"
                        type="date"
                        label-for="data_agendamento"
                        required
                ></b-form-input>
            </b-form-group>

            <b-form-group
                    label="Data da consulta:"
                    label-for="data_consulta"
                    label-cols-lg="6"
                    label-align="right"
            >
                <b-form-input
                        id="data_consulta"
                        v-model="form.data_consulta"
                        type="date"
                        required
                ></b-form-input>
            </b-form-group>

            <b-form-group
                    label="Idade:"
                    label-cols-lg="6"
                    label-align="right"
            >
                <b-form-input
                        v-model="form.idade"
                        type="number"
                        min="0"
                        max="95"
                        required
                ></b-form-input>
            </b-form-group>

            <b-form-group label="Gênero:"
                          label-cols-lg="6"
                          label-align="right"

            >
                <b-form-radio-group id="radio-group-2" v-model="form.genero" name="genero">
                    <b-form-radio value="0">Feminino</b-form-radio>
                    <b-form-radio value="1">Masculino</b-form-radio>
                </b-form-radio-group>
            </b-form-group>

            <b-form-group label="Bolsa família:"
                          label-cols-lg="6"
                          label-align="right"

            >
                <b-form-radio-group id="radio-group-2" v-model="form.auxilio_bolsa_familia" name="radio-sub-component">
                    <b-form-radio value="1">Sim</b-form-radio>
                    <b-form-radio value="0">Não</b-form-radio>
                </b-form-radio-group>
            </b-form-group>

            <b-form-group label="Hipertensão:"
                          label-cols-lg="6"
                          label-align="right"

            >
                <b-form-radio-group id="radio-group-2" v-model="form.hipertensao" name="hipertensao">
                    <b-form-radio value="1">Sim</b-form-radio>
                    <b-form-radio value="0">Não</b-form-radio>
                </b-form-radio-group>
            </b-form-group>

            <b-form-group label="Alcoolismo:"
                          label-cols-lg="6"
                          label-align="right"

            >
                <b-form-radio-group id="radio-group-2" v-model="form.alcolismo" name="alcolismo">
                    <b-form-radio value="1">Sim</b-form-radio>
                    <b-form-radio value="0">Não</b-form-radio>
                </b-form-radio-group>
            </b-form-group>

            <b-form-group label="Deficiência:"
                          label-cols-lg="6"
                          label-align="right"

            >
                <b-form-radio-group id="radio-group-2" v-model="form.deficienca" name="deficienca">
                    <b-form-radio value="1">Sim</b-form-radio>
                    <b-form-radio value="0">Não</b-form-radio>
                </b-form-radio-group>
            </b-form-group>

            <b-form-group label="Diabetes:"
                          label-cols-lg="6"
                          label-align="right"

            >
                <b-form-radio-group id="radio-group-2" v-model="form.diabetes" name="diabetes">
                    <b-form-radio value="1">Sim</b-form-radio>
                    <b-form-radio value="0">Não</b-form-radio>
                </b-form-radio-group>
            </b-form-group>

            <b-form-group label="Recebeu lembrete por SMS:"
                          label-cols-lg="6"
                          label-align="right"

            >
                <b-form-radio-group id="radio-group-2" v-model="form.sms_recebido" name="sms_recebido">
                    <b-form-radio value="1">Sim</b-form-radio>
                    <b-form-radio value="0">Não</b-form-radio>
                </b-form-radio-group>
            </b-form-group>
            <b-button type="submit" size="lg" variant="primary" class="m-2">
                Prever
                 <b-spinner v-if="loading" type="grow"></b-spinner>
            </b-button>
            <b-button type="reset" size="lg" variant="outline-danger" class="m-2">Limpar</b-button>
        </b-form>
        <b-alert v-if="noShow === 'No'" show variant="danger" class="mt-5">
            Provável não comparecimento à consulta!
        </b-alert>
        <b-alert v-if="noShow === 'Yes'" show variant="success" class="mt-5">
            Provável comparecimento à consulta!
        </b-alert>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                form: {
                    data_agendamento: undefined,
                    data_consulta: undefined,
                    idade: undefined,
                    genero: '0',
                    auxilio_bolsa_familia: '0',
                    hipertensao: '0',
                    alcolismo: '0',
                    deficienca: '0',
                    sms_recebido: '0',
                    diabetes: '0'
                },
                loading: false,
                show: true,
                showResult: false,
                noShow: false,
            }
        },
        methods: {
            onSubmit(evt) {
                evt.preventDefault();
                this.loading = true;
                axios.post(`https://medical-appointment-ml.herokuapp.com/predict`, {
                    body: [this.form]
                })
                    .then(r => {
                        if (r.data) {
                            this.noShow = r.data[0]['Dummy'];
                        }
                        this.loading = false;
                    })
                    .catch(e => {
                        this.loading = false;
                        this.errors.push(e)
                    })
            },
            onReset(evt) {
                evt.preventDefault()
                this.form = {
                    data_agendamento: undefined,
                    data_consulta: undefined,
                    idade: undefined,
                    genero: '0',
                    auxilio_bolsa_familia: '0',
                    hipertensao: '0',
                    alcolismo: '0',
                    deficienca: '0',
                    sms_recebido: '0',
                    diabetes: '0',
                };
                this.loading = false;
                this.noShow = undefined;
                this.show = false;
                this.$nextTick(() => {
                    this.show = true
                })
            }
        }
    }
</script>
