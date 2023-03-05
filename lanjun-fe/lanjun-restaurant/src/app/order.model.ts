export class Order {
    order_id!: string;
    user_id!: string;
    cost!: number;
    prepaid!: boolean;
    created_at!: Date;
    items!: string[];
}