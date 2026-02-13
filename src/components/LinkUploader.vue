<script setup lang="ts">
  import { Field, Form, ErrorMessage } from 'vee-validate';

  import { ref } from 'vue';

  const link = ref('');
  const errorHandler = ref('');
  const loading = ref(false);

  async function onSubmit(values: Record<string, unknown>) {
    console.log("Values: ", values, typeof values);
    const link = values.link as string;
    uploadLink(link);
  }


  async function uploadLink(link: string) {

    loading.value = true;
    await fetch('http://localhost:8000/api/spotify/callback/', {
      method: 'POST',
      body: JSON.stringify({ link: link }),
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': '{{ csrf_token }}',
      },
    }).
    then(response => response.json()).
    then(data => {

      // since we have also internal error handling in the backend, we can use the error field to display the error message
      if(data.error) {
        errorHandler.value = data.error;
      } else {
        errorHandler.value = '';
      }
    }).catch(error => {
      errorHandler.value = error.message || 'An error occurred while uploading the link';
    }).finally(() => {
      loading.value = false;
    });

  }

  function linkCheck(value: string) {
    if (value.length > 0) {
      return true;
    }
    return 'This is required';
  }
</script>

<template>
  <div class="flex flex-col items-center justify-center gap-4">

    <!-- if we have an error... -->
    <div v-if="errorHandler" role="alert" class="alert alert-error mt-4">
      <Icon icon="mdi:alert-circle" class="h-6 w-6 shrink-0 stroke-current" />
      <div>
        <p class="font-bold">Oops! Something went wrong...</p>
        <p class="text-sm">{{ errorHandler }}</p>
      </div>
    </div>

    <!-- if we are loading... -->
    <div v-if="loading" class="flex justify-center items-center transition ease-in-out">
      <span class="loading loading-spinner loading-xl transition ease-in-out"></span>
    </div>

    <Form class="fieldsetborder p-4"  @submit="onSubmit">
      <div class="join">
        <Field
            v-model="link"
            type="url"
            name="link"
            :rules="linkCheck"
            class="input join-item"
            required
            placeholder="https://"
            pattern="^(https?://)?([a-zA-Z0-9]([a-zA-Z0-9\-].*[a-zA-Z0-9])?\.)+[a-zA-Z].*$"
        />
        <button class="btn btn-primary join-item">Upload</button>
      </div>
      <ErrorMessage name="link" class="validator-hint"/>

    </Form>

  </div>
</template>
