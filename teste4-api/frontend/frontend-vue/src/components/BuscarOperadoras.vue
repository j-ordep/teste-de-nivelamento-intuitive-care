<script setup lang="ts">
import { ref } from 'vue';

// Interface para os dados da operadora
interface Operadora {
  CNPJ: string;
  Nome_Fantasia: string;
}

const cnpjBusca = ref('');
const operadora = ref<Operadora | null>(null);

const buscar = async () => {
  try {
    const response = await fetch(`http://127.0.0.1:5000/api/operadoras/${cnpjBusca.value}`);
    if (response.ok) {
      operadora.value = await response.json();
    } else {
      operadora.value = null;
      console.error("Operadora não encontrada.");
    }
  } catch (error) {
    console.error("Erro ao buscar operadora:", error);
  }
};
</script>

<template>
  <div class="container">
    <h1>Buscar Operadora por CNPJ</h1>
    <div class="search-bar">
      <input v-model="cnpjBusca" placeholder="Digite o CNPJ da operadora" />
      <button @click="buscar">Buscar</button>
    </div>
    <div v-if="operadora" class="operadora-detalhe">
      <strong>{{ operadora.Nome_Fantasia }}</strong> - CNPJ: {{ operadora.CNPJ }}
    </div>
    <div v-else-if="cnpjBusca" class="operadora-detalhe">
      <p>Operadora não encontrada.</p>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  text-align: center;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

h1 {
  font-weight: 500;
  font-size: 2.6rem;
  margin-bottom: 20px;
}

.search-bar {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 20px;
}

input {
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  flex: 1;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.operadora-detalhe {
  margin-top: 20px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f9f9f9;
}
</style>
