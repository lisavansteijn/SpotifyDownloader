<script setup lang="ts">
  import { ref } from 'vue';
  import { Field, Form, ErrorMessage } from 'vee-validate';

  const link = ref('');

  async function onSubmit(values: any) {
    if (values.link) {
      await uploadLink(values);
    }
  }

  async function uploadLink(values: any) {

    const link = String(values.link);
    console.log("Link: ", link);
    const response = await fetch('http://localhost:8000/api/upload-link/', {
      method: 'POST',
      body: JSON.stringify({ link: link }),
      headers: {
        'Content-Type': 'application/json',
      },
    });
    console.log("Response: ", response);
    const data = await response.json();
    console.log("Data: ", data);
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

    <Form class="fieldsetborder p-4"  @submit="onSubmit">
      <div class="join">
        <Field
            type="url"
            name="link"
            :rules="linkCheck"
            class="input join-item"
            required
            placeholder="https://"
            v-model="link"
            pattern="^(https?://)?([a-zA-Z0-9]([a-zA-Z0-9\-].*[a-zA-Z0-9])?\.)+[a-zA-Z].*$"
        />
        <button class="btn btn-primary join-item">Upload</button>
      </div>
      <ErrorMessage name="link" class="validator-hint"/>

    </Form>

  </div>
</template>
